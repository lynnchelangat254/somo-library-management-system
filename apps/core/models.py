from django.db import models

from apps.utils.base import BaseModel


class Newsletter(BaseModel):
    email = models.EmailField(max_length=255)

    class Meta:
        verbose_name_plural = "Newsletters"
        ordering = ["-created_at"]

    def __str__(self):
        return self.email
