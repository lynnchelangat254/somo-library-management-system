from typing import ClassVar

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.users.managers import UserManager
from apps.utils.base import BaseModel


class User(AbstractUser, BaseModel):
    """
    Default custom user model for dasce-ecommerce-api.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    class Roles(models.TextChoices):
        ADMIN = "Admin", "Admin"
        MEMBER = "Member", "Member"
        LIBRARIAN = "Librarian", "Librarian"

    # First and last name do not cover name patterns around the globe
    first_name = models.CharField(
        _("First Name"), max_length=255, blank=True, null=True
    )
    last_name = models.CharField(_("Last Name"), max_length=255, blank=True, null=True)
    email = models.EmailField(_("email address"), unique=True, max_length=255)
    username = models.CharField(_("Username"), max_length=255)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    role = models.CharField(_("Role"), choices=Roles, max_length=255)
    is_active = models.BooleanField(_("Is active"), default=True)
    is_admin = models.BooleanField(_("Is admin"), default=False)
    is_superuser = models.BooleanField(_("Is superuser"), default=False)
    is_staff = models.BooleanField(_("Is staff"), default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects: ClassVar[UserManager] = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None) -> bool:
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label) -> bool:
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def get_full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
