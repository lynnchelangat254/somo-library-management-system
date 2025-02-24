from django.contrib import admin

from apps.members.models import Member


class MemberAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "membership_start_date",
        "membership_end_date",
        "membership_type",
        "membership_status",
        "date_approved",
        "approved_by",
    )
    list_per_page = 20


admin.site.register(Member, MemberAdmin)
