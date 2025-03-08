from django.urls import path

from apps.reservations import views


urlpatterns = [
    path(
        "member/<str:member_id>/reserve/<str:book_id>/send/",
        views.reserve_book,
        name="reserve-book",
    ),
    path(
        "member/<str:member_id>/reserve/<str:book_id>/cancel/",
        views.cancel_reservation,
        name="cancel-reservation",
    ),
    path("member/reservations/", views.get_reservations, name="member-reservations"),
    path("librarian/reservations/", views.get_reservations, name="librarian-reservations"),
    path(
        "librarian/reservations/<str:reservation_id>/",
        views.get_reservations,
        name="get-reservation",
    ),
    path(
        "librarian/reservations/<str:reservation_id>/update/",
        views.update_reservation,
        name="my-reservations",
    ),
]
