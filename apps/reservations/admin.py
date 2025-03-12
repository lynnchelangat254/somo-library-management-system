from django.contrib import admin

from apps.reservations.models import Reservation


class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "status",
        "waiting_position",
        "reservation_date",
    )
    list_per_page = 20


admin.site.register(Reservation, ReservationAdmin)
