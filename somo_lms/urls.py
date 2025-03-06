from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("apps.users.urls")),
    path("", include("apps.core.urls")),
    path("books/", include("apps.books.urls")),
    path("", include("apps.members.urls")),
    path("", include("apps.transactions.urls")),
    path("", include("apps.reservations.urls")),
    path("", include("apps.notifications.urls")),
    path("", include("apps.librarians.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
