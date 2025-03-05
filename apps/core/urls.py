from django.urls import path

from apps.core.views import home, librarian_dashboard, member_dashboard

urlpatterns = [
    path("", home, name="home"),
    path("librarian/", librarian_dashboard, name="librarian-dashboard"),
    path("member/", member_dashboard, name="member-dashboard"),
]
