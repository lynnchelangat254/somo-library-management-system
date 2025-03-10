from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from apps.books.models import Book
from apps.books.forms import BookForm
from apps.utils.permissions import is_librarian
from apps.transactions.models import Transaction

from datetime import datetime


def get_books(request, *args, **kwargs):
    # Fetch all objects from the model
    book_list = Book.objects.all()

    # Set up pagination
    paginator = Paginator(book_list, 20)  # Show 20 objects per page
    page_number = request.GET.get("page")  # Get the page number from the request
    books = paginator.get_page(page_number)  # Get the page object

    return render(request, "books.html", {"books": books})


def get_book(request, *args, **kwargs):
    book_id = kwargs.get("id")  # Get the book ID from the URL
    book = Book.objects.filter(id=book_id).first()  # Fetch the book object

    return render(request, "book_detail.html", {"book": book})


@login_required(login_url="login")
@is_librarian
def add_book(request, *args, **kwargs):
    # Add a new book to the database
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Book added successfully!")
            return redirect("librarian-books")
    form = BookForm()
    return render(request, "add_book.html", {"form": form})


@login_required(login_url="login")
@is_librarian
def get_librarian_books(request, *args, **kwargs):
    # Fetch all objects from the model
    book_list = Book.objects.all()
    # Set up pagination
    paginator = Paginator(book_list, 20)  # Show 20 objects per page
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
    paginator = Paginator(book_list, 20)  # Show 20 objects per page
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
        form = BookForm(request.POST, instance=book)
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
