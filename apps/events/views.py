from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages

from apps.utils.permissions import is_librarian, is_member
from apps.events.models import Event, EventRegistration
from apps.events.forms import EventForm
from apps.members.models import Member


def get_events(request, *args, **kwargs):
    # Fetch all events from the database
    event_list = Event.objects.all()

    # paginate events
    paginator = Paginator(event_list, 15)
    page_number = request.GET.get("page")
    events = paginator.get_page(page_number)

    return render(request, "events.html", {"events": events})


def get_event(request, *args, **kwargs):
    # Fetch a specific event from the database
    event = Event.objects.filter(pk=kwargs.get("event_id")).first()
    member = None

    if request.user.is_authenticated:
        member = Member.objects.filter(user=request.user).first()
    # check if member is already a participant
    is_participant = EventRegistration.objects.filter(participant=member).exists()

    if event is None:
        return redirect("events")
    return render(
        request, "event_detail.html", {"event": event, "is_participant": is_participant}
    )


@login_required
@is_member
def register_event_member(request, *args, **kwargs):
    # Register a user for an event by id
    event = Event.objects.filter(id=kwargs.get("event_id")).first()
    member = Member.objects.filter(user=request.user).first()
    if event is None:
        messages.error(request, "Event not found.")
        return redirect("events")

    # check if member is already registered
    if EventRegistration.objects.filter(participant=member).exists():
        messages.error(request, "You have already registered for this event.")
        return redirect("event-detail", event_id=event.id)

    event_registration = EventRegistration.objects.create(
        event=event, participant=member
    )
    event.current_participants = event.current_participants + 1
    event.save()

    messages.success(request, "Registration successful!")
    return redirect("event-detail", event_id=event.id)


@login_required
@is_member
def unregister_event_member(request, *args, **kwargs):
    # Unregister a user for an event by id
    event = Event.objects.filter(id=kwargs.get("event_id")).first()
    member = Member.objects.filter(user=request.user).first()
    if event is None:
        messages.error(request, "Event not found.")
        return redirect("events")
    if not EventRegistration.objects.filter(participant=member, event=event).exists():
        messages.error(request, "You are not registered for this event.")
        return redirect("event-detail", event_id=event.id)
    event_registration = EventRegistration.objects.filter(
        participant=member, event=event
    ).first()
    event_registration.delete()
    event.current_participants = (
        event.current_participants - 1 if event.current_participants >= 1 else 0
    )
    event.save()
    messages.success(request, "Unregistered from the event successfully!")
    return redirect("event-detail", event_id=event.id)


@login_required
@is_librarian
def librarian_get_events(request, *args, **kwargs):
    # Fetch all events from the database
    event_list = Event.objects.all()
    # paginate events
    paginator = Paginator(event_list, 15)
    page_number = request.GET.get("page")
    events = paginator.get_page(page_number)
    return render(request, "librarian_events.html", {"events": events})


@login_required
@is_librarian
def create_event(request, *args, **kwargs):
    # Add a new event to the database
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Event added successfully!")
            return redirect("librarian-events")
        else:
            messages.error(request, "Book not added. Please check the form.")
            return render(request, "create_event.html", {"form": form})
    form = EventForm()
    return render(request, "create_event.html", {"form": form})


@login_required
@is_librarian
def update_event(request, *args, **kwargs):
    # Update an existing event in the database by id
    event = Event.objects.filter(id=kwargs.get("event_id")).first()
    if event is None:
        messages.error(request, "Event not found.")
        return redirect("librarian-events")
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, "Event updated successfully!")
            return redirect("librarian-events")
    form = EventForm(instance=event)
    return render(request, "update_event.html", {"form": form})


@login_required
@is_librarian
def delete_event(request, *args, **kwargs):
    # Delete an event from the database by id
    event_id = kwargs.get("event_id")
    event = Event.objects.filter(pk=event_id).first()
    if event is None:
        messages.error(request, "Event not found.")
        return redirect("librarian-events")

    event.delete()
    messages.success(request, "Event deleted successfully!")
    return redirect("librarian-events")
