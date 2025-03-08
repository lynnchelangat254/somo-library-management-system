from typing import ClassVar

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.users.managers import UserManager
from apps.utils.base import BaseModel
from apps.utils.constants import COUNTRIES
from apps.utils.helper import validate_phone_number


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

    class GENDERS(models.TextChoices):
        MALE = "Male", "Male"
        FEMALE = "Female", "Female"

    # First and last name do not cover name patterns around the globe
    first_name = models.CharField(_("First name"), max_length=255)
    last_name = models.CharField(_("Last name"), max_length=255)
    email = models.EmailField(_("Email address"), unique=True, max_length=255)
    username = models.CharField(_("Username"), max_length=255)
    phone_number = models.CharField(
        _("Phone number"), max_length=17, validators=[validate_phone_number]
    )
    country = models.CharField(_("Country"), max_length=255, choices=COUNTRIES)
    city = models.CharField(_("City"), max_length=255)
    role = models.CharField(_("Role"), choices=Roles, max_length=255)
    gender = models.CharField(_("Gender"), max_length=255, choices=GENDERS)
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
