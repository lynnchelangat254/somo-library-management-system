from django.db import models

from apps.utils.base import BaseModel


class Notification(BaseModel):

    class NotificationTypes(models.TextChoices):
        RESERVATION_ALERT = "Reservation Alert", "Reservation Alert"
        SYSTEM_NOTIFICATION = "System Notification", "System Notification"
        DUE_DATE = "DUE Date", "DUE Date"

    title = models.CharField(max_length=255)
    message = models.TextField(max_length=1000)
    type = models.CharField(max_length=255, choices=NotificationTypes)
    read = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Notifications"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
