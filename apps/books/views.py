from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import render

from apps.books.models import Book

def get_books(request, *args, **kwargs):
    # Fetch all objects from the model
    book_list = Book.objects.all()

    # Set up pagination
    paginator = Paginator(book_list, 20)  # Show 20 objects per page
    page_number = request.GET.get("page")  # Get the page number from the request
    page_obj = paginator.get_page(page_number)  # Get the page object

    return render(request, "books.html", {"page_obj": page_obj})


def get_book(request, *args, **kwargs):
    book_id = kwargs.get("id")  # Get the book ID from the URL
    book = Book.objects.filter(id=book_id).first()  # Fetch the book object

    return render(request, "book_detail.html", {"book": book})
