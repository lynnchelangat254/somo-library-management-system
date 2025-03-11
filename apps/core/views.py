from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from apps.members.models import Member
from apps.notifications.models import Notification
from apps.reservations.models import Reservation
from apps.transactions.models import Transaction
from apps.librarians.models import Librarian
from apps.books.models import Book
from apps.utils.permissions import is_librarian, is_member


def home(request):
    return render(request, "landing_page.html", {})


@login_required(login_url="login")
@is_member
def member_dashboard(request):
    member = Member.objects.filter(user=request.user).first()
    reservations = Reservation.objects.filter(member=member).count()
    borrowed_books = Transaction.objects.filter(
        status="Borrowed", member=member
    ).count()
    returned_books = Transaction.objects.filter(
        status="Returned", member=member
    ).count()
    overdue_books = Transaction.objects.filter(status="Overdue", member=member).count()
    lost_books = Transaction.objects.filter(status="Lost", member=member).count()

    return render(
        request,
        "member_dashboard_home.html",
        {
            "member": member,
            "reservations": reservations,
            "borrowed_books": borrowed_books,
            "returned_books": returned_books,
            "overdue_books": overdue_books,
            "lost_books": lost_books,
        },
    )


@login_required(login_url="login")
@is_librarian
def librarian_dashboard(request):

    librarian = Librarian.objects.filter(user=request.user).first()
    notifications = Notification.objects.all()
    book_reservations = Reservation.objects.all().count()
    borrowed_books = Transaction.objects.filter(status="Borrowed").count()
    returned_books = Transaction.objects.filter(status="Returned").count()
    overdue_books = Transaction.objects.filter(status="Overdue").count()
    lost_books = Transaction.objects.filter(status="Lost").count()
    number_of_members = Member.objects.all().count()
    number_of_books = Book.objects.all().count()

    return render(
        request,
        "librarian_dashboard_home.html",
        {
            "librarian": librarian,
            "notifications": notifications,
            "borrowed_books": borrowed_books,
            "returned_books": returned_books,
            "overdue_books": overdue_books,
            "lost_books": lost_books,
            "number_of_members": number_of_members,
            "book_reservations": book_reservations,
            "number_of_books": number_of_books,
        },
    )
