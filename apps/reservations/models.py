from django.db import models

from apps.utils.base import BaseModel
from apps.books.models import Book
from apps.members.models import Member


class Reservation(BaseModel):
    class ReservationStatus(models.TextChoices):
        PENDING = "Pending", "Pending"
        FULFILLED = "Fulfilled", "Fulfilled"
        CANCELLED = "Cancelled", "Cancelled"

    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="reservations"
    )
    member = models.ForeignKey(
        Member, on_delete=models.CASCADE, related_name="member_reservation"
    )
    status = models.CharField(
        max_length=255, choices=ReservationStatus, default=ReservationStatus.PENDING
    )
    waiting_position = models.IntegerField(default=1)
    reservation_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Reservations"
        ordering = ["-reservation_date"]

    def __str__(self):
        return f"{self.book.title}"
