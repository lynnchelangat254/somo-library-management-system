from django.urls import path

from apps.reservations import views


urlpatterns = [
    path(
        "member/reservations/<str:reservation_id>/cancel/",
        views.cancel_reservation,
        name="cancel-reservation",
    ),
    path(
        "librarian/reservations/", views.get_reservations, name="librarian-reservations"
    ),
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
    path(
        "member/reservations/",
        views.member_reservations,
        name="member-reservations",
    ),
]
