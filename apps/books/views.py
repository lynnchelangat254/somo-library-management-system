from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.urls import reverse

from apps.books.models import Book, BookGenre
from apps.books.forms import BookForm
from apps.utils.permissions import is_librarian, is_member
from apps.transactions.models import Transaction
from apps.reservations.models import Reservation
from apps.members.models import Member

from datetime import datetime, timedelta


def get_books(request, *args, **kwargs):
    # Fetch all objects from the model
    genre = request.GET.get("genre")
    query = request.GET.get("query")

    # filter out books by genres
    if genre:
        book_list = Book.objects.filter(genre__name=genre)
    else:
        book_list = Book.objects.all()
        genre = "All"
    genres = BookGenre.objects.all()

    if query:
        book_list = book_list.filter(
            Q(title__icontains=query)
            | Q(author__icontains=query)
            | Q(description__icontains=genre)
        )

    # Set up pagination
    paginator = Paginator(book_list, 10)  # Show 20 objects per page
    page_number = request.GET.get("page")  # Get the page number from the request
    books = paginator.get_page(page_number)  # Get the page object

    return render(
        request,
        "books.html",
        {"books": books, "genres": genres, "current_genre": genre},
    )


def get_book(request, *args, **kwargs):
    book_id = kwargs.get("book_id")  # Get the book ID from the URL
    book = Book.objects.filter(id=book_id).first()  # Fetch the book object

    return render(request, "book_detail.html", {"book": book})


@login_required(login_url="login")
@is_member
def borrow_book(request, *args, **kwargs):
    book_id = kwargs.get("book_id")  # Get the book ID from the URL
    book = Book.objects.filter(id=book_id).first()  # Fetch the book object
    duration = request.POST.get("duration")
    format = request.POST.get("format")

    # check if the book exists in the database
    if book is None:
        messages.error(request, "Book not found!")
        return redirect("books")

    # check if the member has already borrowed this book
    if Transaction.objects.filter(book=book, member__user=request.user).exists():
        messages.error(request, "You have already borrowed this book!")
        return redirect(reverse("book-detail", kwargs={"book_id": book_id}))
    # check if the book is available for borrowing
    if book.available_copies == 0:
        messages.error(request, "This book is currently not available!")
        return redirect(reverse("book-detail", kwargs={"book_id": book_id}))
    # create a new transaction for the borrowing
    member = Member.objects.filter(user=request.user).first()  # get member
    return_date = datetime.now() + timedelta(days=float(duration))
    transaction = Transaction(
        book=book,
        member=member,
        book_format=format,
        return_date=return_date,
        borrow_date=datetime.now(),
    )
    transaction.save()
    messages.success(request, "Book borrowed successfully!")
    book.available_copies -= 1
    book.save()
    return redirect(reverse("book-detail", kwargs={"book_id": book_id}))


@login_required(login_url="login")
@is_member
def reserve_book(request, *args, **kwargs):
    book_id = kwargs.get("book_id")  # Get the book ID from the URL
    book = Book.objects.filter(id=book_id).first()  # Fetch the book object

    # check if the book exists in the database
    if book is None:
        messages.error(request, "Book not found.")
        return redirect("books")

    # check if the member has already reserved this book
    if Reservation.objects.filter(book=book, member__user=request.user).exists():
        messages.error(request, "You have already reserved this book.")
        return redirect(reverse("book-detail", kwargs={"book_id": book_id}))

    # create a new reservation for the borrowing
    member = Member.objects.filter(user=request.user).first()
    reservation = Reservation(book=book, member=member)
    # get number of reservations for this book
    book_reservations = Reservation.objects.filter(book=book, status="Pending").count()
    # update the waiting position of the reservation
    reservation.waiting_position = (
        1 if book_reservations == 0 else book_reservations + 1
    )
    reservation.save()
    messages.success(request, "Book reserved successfully!")
    return redirect(reverse("book-detail", kwargs={"book_id": book_id}))


@login_required(login_url="login")
@is_librarian
def add_book(request, *args, **kwargs):
    # Add a new book to the database
    if request.method == "POST":
        form = BookForm(
            request.POST, request.FILES
        )  # Handle file data with request.FILES
        if form.is_valid():
            form.save()
            messages.success(request, "Book added successfully!")
            return redirect("librarian-books")
        else:
            messages.error(request, "Book not added. Please check the form.")
            return render(request, "add_book.html", {"form": form})
    form = BookForm()
    return render(request, "add_book.html", {"form": form})


@login_required(login_url="login")
@is_librarian
def get_librarian_books(request, *args, **kwargs):
    # Fetch all objects from the model
    book_list = Book.objects.all()
    # Set up pagination
    paginator = Paginator(book_list, 15)  # Show 20 objects per page
    page_number = request.GET.get("page")  # Get the page number from the request
    books = paginator.get_page(page_number)  # Get the page object
    return render(request, "librarian_books.html", {"books": books})


@login_required(login_url="login")
@is_librarian
def get_overdue_books(request, *args, **kwargs):
    # Fetch all overdue books
    transaction_list = Transaction.objects.filter(return_date__lt=datetime.now())
    book_list = []
    for transaction in transaction_list:
        book_list.append(transaction.book)

    # Set up pagination
    paginator = Paginator(book_list, 15)  # Show 15 objects per page
    page_number = request.GET.get("page")  # Get the page number from the request
    books = paginator.get_page(page_number)  # Get the page object

    return render(request, "overdue_books.html", {"books": books})


@login_required(login_url="login")
@is_librarian
def update_book(request, *args, **kwargs):
    book_id = kwargs.get("book_id")  # Get the book ID from the URL
    book = Book.objects.filter(id=book_id).first()  # Fetch the book object
    if not book:
        messages.error(request, "Book not found!")
        return redirect("librarian-books")

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, "Book updated successfully!")
            return redirect("librarian-books")

    form = BookForm(instance=book)
    return render(request, "update_book.html", {"form": form, "book": book})


@login_required(login_url="login")
@is_librarian
def delete_book(request, *args, **kwargs):
    book_id = kwargs.get("book_id")  # Get the book ID from the URL
    book = Book.objects.filter(id=book_id).first()  # Fetch the book object

    if not book:
        messages.error(request, "Book not found!")
        return redirect("librarian-books")

    book.delete()
    messages.success(request, "Book deleted successfully!")
    return redirect("librarian-books")


@login_required(login_url="login")
@is_member
def get_borrowed_books(request, *args, **kwargs):
    # Fetch all borrowed books
    transaction_list = Transaction.objects.filter(member__user=request.user)
    book_list = []
    for transaction in transaction_list:
        book_list.append(transaction.book)

    # Set up pagination
    paginator = Paginator(book_list, 15)  # Show 15 objects per page
    page_number = request.GET.get("page")  # Get the page number from the request
    books = paginator.get_page(page_number)  # Get the page object
    return render(request, "borrowed_books.html", {"books": books})
