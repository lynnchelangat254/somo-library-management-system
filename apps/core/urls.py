from django.urls import path

from apps.core import views

urlpatterns = [
    path("", views.home, name="home"),
    path("librarian/", views.librarian_dashboard, name="librarian-dashboard"),
    path("member/", views.member_dashboard, name="member-dashboard"),
    path(
        "newsletter/subscribe/",
        views.subscribe_to_newsletter,
        name="subscribe-to-newsletter",
    ),
]
