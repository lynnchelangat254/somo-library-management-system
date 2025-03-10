from apps.members import views

from django.urls import path

urlpatterns = [
    # librarian dashboard
    path("librarian/members/", views.get_members, name="members"),
    path("librarian/members/<str:member_id>/", views.get_member, name="member-detail"),
    path(
        "librarian/members/<str:member_id>/update/",
        views.update_member,
        name="update-member",
    ),
    path(
        "librarian/members/<str:member_id>/delete/",
        views.delete_member,
        name="delete-member",
    ),
    path("librarian/requests/", views.get_membership_requests, name="membership-requests"),
    path(
        "librarian/requests/<str:member_id>/approve",
        views.approve_membership_request,
        name="approve-membership-request",
    ),
    path(
        "librarian/requests/<str:member_id>/decline",
        views.decline_membership_request,
        name="decline-membership-request",
    ),
]
