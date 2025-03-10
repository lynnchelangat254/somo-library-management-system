from django.urls import path

from apps.books import views

urlpatterns = [
    path("books/", views.get_books, name="books"),
    path("books/<str:book_id>/", views.get_book, name="book-detail"),
    path("librarian/books/", views.get_librarian_books, name="librarian-books"),
    path(
        "librarian/overdue-books/",
        views.get_overdue_books,
        name="librarian-overdue-books",
    ),
    path("librarian/books/add/", views.add_book, name="add-book"),
    path(
        "librarian/books/update/<str:book_id>/", views.update_book, name="update-book"
    ),
    path(
        "librarian/books/delete/<str:book_id>/", views.delete_book, name="delete-book"
    ),
]
