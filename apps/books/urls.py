from django.urls import path

from apps.books.views import get_books, get_book

urlpatterns = [
    path("", get_books, name="books"),
    path("<str:id>/", get_book, name="book-detail"),
]
