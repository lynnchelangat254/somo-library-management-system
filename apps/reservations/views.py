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
    paginator = Paginator(reservation_list, 20)  # Show 20 objects per page
    page_number = request.GET.get("page")  # Get the page number from the request
    reservations = paginator.get_page(page_number)  # Get the page object

    return render(request, "reservations.html", {"reservations": reservations})


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
def reserve_book(request, *args, **kwargs):
    # Reserve a book for a member
    book_id = kwargs.get("book_id")
    member_id = kwargs.get("member_id")
    waiting_position = Reservation.objects.filter(book_id=book_id).count() + 1
    reservation = Reservation.objects.create(
        book_id=book_id, member_id=member_id, waiting_position=waiting_position
    )
    messages.success(
        request, f"Reservation for book {reservation.book.title} made successfully."
    )
    return redirect("member-dashboard")


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
