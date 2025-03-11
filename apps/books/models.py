from django.db import models

from apps.utils.base import BaseModel
from tinymce.models import HTMLField


class BookFormat(BaseModel):
    class FormatChoices(models.TextChoices):
        PAPERBACK = "Paperback", "Paperback"
        AUDIO_BOOK = "Audio Book", "Audio Book"
        EBOOK = "Ebook", "Ebook"
        HARDCOVER = "Hardcover", "Hardcover"

    name = models.CharField(max_length=255, choices=FormatChoices)

    class Meta:
        verbose_name_plural = "Book Formats"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name


class BookGenre(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    description = HTMLField()

    class Meta:
        verbose_name_plural = "Genres"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Book(BaseModel):
    class Languages(models.TextChoices):
        ENGLISH = "English"
        FRENCH = "French"
        SPANISH = "Spanish"

    title = models.CharField(max_length=255, unique=True)
    description = HTMLField()
    author = models.CharField(max_length=255)
    genre = models.ForeignKey(
        BookGenre,
        max_length=255,
        related_name="genres",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    isbn = models.CharField(max_length=255)

    language = models.CharField(
        max_length=255, choices=Languages, default=Languages.ENGLISH
    )
    edition = models.CharField(max_length=255, null=True, blank=True)
    formats = models.ManyToManyField(BookFormat, blank=True)
    publisher_name = models.CharField(max_length=255, null=True, blank=True)
    publisher_address = models.CharField(max_length=255, null=True, blank=True)
    published_date = models.DateField(null=True, blank=True)
    available_copies = models.PositiveIntegerField(default=0)
    total_copies = models.PositiveIntegerField()
    cover_image = models.ImageField(upload_to="covers/%Y%m%d", null=True, blank=True)

    class Meta:
        verbose_name_plural = "Books"
        ordering = ["title"]

    def __str__(self):
        return self.title


class BookFiles(BaseModel):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="book_files")
    file = models.FileField(upload_to="books/%Y%m%d")

    class Meta:
        verbose_name_plural = "Book Files"

    def save(self, *args, **kwargs):
        file_format = str(self.file.name).split(".")[-1]
        self.file.name = f"{self.book.name}_{self.book.id}_{file_format}"
        super().save(*args, **kwargs)
