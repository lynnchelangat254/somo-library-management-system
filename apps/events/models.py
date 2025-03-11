from django.db import models

from apps.utils.base import BaseModel
from apps.members.models import Member


class Event(BaseModel):

    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="events/%Y%m%d")
    max_participants = models.IntegerField(default=50)
    current_participants = models.IntegerField(default=0)
    event_date = models.DateField()

    class Meta:
        verbose_name_plural = "Events"
        ordering = ["-event_date"]

    def __str__(self):
        return f"{self.name} - {self.event_date}"


class EventRegistration(BaseModel):

    class Status(models.TextChoices):
        REGISTERED = "Registered", "Registered"
        ATTENDED = "Attended", "Attended"
        CANCELLED = "Cancelled", "Cancelled"

    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    participant = models.ForeignKey(Member, related_name="event_member", on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, choices=Status)

    class Meta:
        verbose_name_plural = "Registrations"
        ordering = ["-registration_date"]

    def __str__(self):
        return f"{self.participant} - {self.event}"
