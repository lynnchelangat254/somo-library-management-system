from django.contrib import admin

from apps.members.models import Member


class MemberAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "membership_type",
        "membership_status",
        "approval_date",
        "approved_by",
    )
    list_per_page = 20


admin.site.register(Member, MemberAdmin)
