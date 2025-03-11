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
    path("member/borrowed-books/", views.get_borrowed_books, name="borrowed-books"),
    path("member/borrow/<str:book_id>/", views.borrow_book, name="borrow-book"),
    path("member/reserve/<str:book_id>/", views.reserve_book, name="return-book"),
]
