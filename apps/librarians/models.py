from django.db import models

from apps.utils.base import BaseModel
from apps.users.models import User


class Librarian(BaseModel):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="librarian"
    )
    librarian_image = models.ImageField(
        upload_to="librarians/%Y%m%d", null=True, blank=True
    )
    employee_id = models.IntegerField(unique=True)
    date_hired = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Librarian"
        verbose_name_plural = "Librarians"

    def __str__(self):
        return f"{self.user.username} (Librarian)"
