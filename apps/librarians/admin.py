from django.contrib import admin


from apps.librarians.models import Librarian


class LibrarianAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "employee_id",
        "date_hired",
    )
    list_per_page = 20


admin.site.register(Librarian, LibrarianAdmin)
