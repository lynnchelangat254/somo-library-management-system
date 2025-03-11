from django.contrib import admin

from apps.events.models import Event, EventRegistration


class EventAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "description",
        "event_date",
    )
    list_per_page = 20


class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "event",
        "registration_date",
    )
    list_per_page = 20


admin.site.register(Event, EventAdmin)
admin.site.register(EventRegistration, EventRegistrationAdmin)
