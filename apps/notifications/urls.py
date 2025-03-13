from django.urls import path

from apps.notifications import views

urlpatterns = [
    path("member/notifications/", views.get_notifications, name="notifications"),
    path(
        "member/notifications/<str:notification_id>/update/",
        views.update_notification,
        name="update-notification",
    ),
]
