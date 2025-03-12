from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from apps.reservations.models import Reservation
from apps.reservations.forms import ReservationForm
from apps.utils.permissions import is_librarian, is_member


@login_required(login_url="login")
@is_librarian
def get_reservations(request, *args, **kwargs):
    # Fetch all objects from the model
    reservation_list = Reservation.objects.all()
    # paginate the list
    paginator = Paginator(reservation_list, 15)  # Show 20 objects per page
    page_number = request.GET.get("page")  # Get the page number from the request
    reservations = paginator.get_page(page_number)  # Get the page object

    return render(request, "reservations.html", {"reservations": reservations})


@login_required(login_url="login")
@is_member
def member_reservations(request, *args, **kwargs):
    # Fetch all objects from the model
    reservation_list = Reservation.objects.filter(member__user=request.user)
    # paginate the list
    paginator = Paginator(reservation_list, 15)  # Show 20 objects per page
    page_number = request.GET.get("page")  # Get the page number from the request
    reservations = paginator.get_page(page_number)  # Get the page object
    return render(request, "member_reservations.html", {"reservations": reservations})


@login_required(login_url="login")
@is_librarian
def get_reservation(request, *args, **kwargs):
    # Fetch the reservation object
    reservation_id = kwargs.get("reservation_id")
    reservation = Reservation.objects.filter(id=reservation_id).first()
    return render(request, "reservation_detail.html", {"reservation": reservation})


@login_required(login_url="login")
@is_librarian
def update_reservation(request, *args, **kwargs):
    # Update the reservation object
    reservation_id = kwargs.get("reservation_id")
    reservation = Reservation.objects.filter(id=reservation_id).first()
    if request.method == "POST":
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect("reservations")
    else:
        form = ReservationForm(instance=reservation)
    return render(request, "update_reservation.html", {"form": form})


@login_required(login_url="login")
@is_member
def cancel_reservation(request, *args, **kwargs):
    # Cancel a reservation for a member
    reservation_id = kwargs.get("reservation_id")
    reservation = Reservation.objects.filter(id=reservation_id).first()
    if reservation is None:
        messages.error(request, "Reservation not found.")
        return redirect("member-dashboard")

    messages.success(
        request, f"Reservation for book {reservation.book.title} canceled successfully."
    )
    reservation.delete()
    return redirect("member-dashboard")
