from django.urls import path

from apps.events import views

urlpatterns = [
    path("events/", views.get_events, name="events"),
    path("events/<str:event_id>/", views.get_event, name="event-detail"),
    path(
        "events/<str:event_id>/register/",
        views.register_event_member,
        name="register-event-member",
    ),
    path(
        "events/<str:event_id>/unregister/",
        views.unregister_event_member,
        name="unregister-event-member",
    ),
    path("librarian/events/", views.librarian_get_events, name="librarian-events"),
    path(
        "librarian/events/<str:event_id>/update/",
        views.update_event,
        name="update-event",
    ),
    path(
        "librarian/events/<str:event_id>/delete/",
        views.delete_event,
        name="delete-event",
    ),
    path("librarian/events/add/", views.create_event, name="add-event"),
]
