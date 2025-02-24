from django.contrib import admin

from apps.books.models import Book, BookGenre, BookFormat, BookFiles


class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "published_date", "genre")
    search_fields = ("title", "author", "genre__name")
    list_filter = ("published_date", "genre")
    list_per_page = 20


class BookGenresAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at", "updated_at")
    search_fields = ("name",)
    list_per_page = 20


class BookFormatAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at", "updated_at")
    search_fields = ("name",)
    list_per_page = 20


class BookFilesAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at", "updated_at")
    list_per_page = 20


# register models
admin.site.register(Book, BookAdmin)
admin.site.register(BookGenre, BookGenresAdmin)
admin.site.register(BookFormat, BookFormatAdmin)
admin.site.register(BookFiles, BookFilesAdmin)
