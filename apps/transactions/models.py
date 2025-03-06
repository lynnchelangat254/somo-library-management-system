from django.db import models

from apps.utils.base import BaseModel
from apps.books.models import Book
from apps.members.models import Member


class Transaction(BaseModel):
    class TransactionStatus(models.TextChoices):
        BORROWED = "Borrowed", "Borrowed"
        RETURNED = "Returned", "Returned"
        OVERDUE = "Overdue", "Overdue"
        LOST = "Lost", "Lost"

    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="book_transaction"
    )
    member = models.ForeignKey(
        Member, on_delete=models.CASCADE, related_name="member_transaction"
    )
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)
    fine_amount = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    status = models.CharField(
        max_length=255, choices=TransactionStatus, default=TransactionStatus.BORROWED
    )

    class Meta:
        verbose_name_plural = "Transaction"
        ordering = ["-borrow_date"]

    def __str__(self):
        return f"{self.book.name}  {self.borrow_date}"
