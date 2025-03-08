from django.db import models

from apps.users.models import User
from apps.utils.base import BaseModel
from apps.librarians.models import Librarian


class Member(BaseModel):
    class MembershipStatus(models.TextChoices):
        PENDING = "Pending", "Pending"
        Approved = "Approved", "Approved"
        SUSPENDED = "Suspended", "Suspended"
        DECLINED = "Declined", "Declined"

    class MembershipTypes(models.TextChoices):
        Standard = "Standard", "Standard"
        Premium = "Premium", "Premium"

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="members")
    member_image = models.ImageField(upload_to="members/%Y%m%d", null=True, blank=True)
    membership_type = models.CharField(
        max_length=255, choices=MembershipTypes, default=MembershipTypes.Standard
    )
    membership_status = models.CharField(
        max_length=255, choices=MembershipStatus, default=MembershipStatus.PENDING
    )
    approval_date = models.DateField(null=True, blank=True)
    approved_by = models.ForeignKey(
        Librarian,
        related_name="approval_by",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Member"
        verbose_name_plural = "Members"
        ordering = ["-approval_date"]

    def __str__(self):
        return f"{self.user.get_full_name()}  ({self.membership_type})"
