from django.contrib import admin


from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.utils.translation import gettext_lazy as _


from apps.users.models import User


class UserAdminManager(auth_admin.UserAdmin):

    model = User
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "password",
                )
            },
        ),
        (
            "Personal info",
            {
                "fields": (
                    "username",
                    "first_name",
                    "last_name",
                    "phone_number",
                    "country",
                    "city",
                    "role",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_admin",
                    "is_staff",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "first_name",
                    "last_name",
                    "role",
                    "email",
                    "password1",
                    "password2",
                    "is_active",
                    "is_admin",
                    "is_staff",
                ),
            },
        ),
    )
    list_display = (
        "email",
        "username",
        "is_active",
        "is_admin",
        "is_staff",
    )
    list_filter = ("is_active", "is_admin", "is_staff")
    search_fields = ("first_name", "last_name")
    filter_horizontal = ()
    list_per_page = 20


admin.site.register(User, UserAdminManager)
