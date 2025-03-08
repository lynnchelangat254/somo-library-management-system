from django import forms
from .models import (
    BookGenre,
    BookFormat,
    Book,
)  # Make sure these are imported from your models
from tinymce.widgets import TinyMCE  # If you're using the TinyMCE editor for HTMLField


class BookForm(forms.ModelForm):
    class Meta:
        model = Book  # Replace with the actual model name
        fields = [
            "title",
            "description",
            "author",
            "genre",
            "isbn",
            "language",
            "edition",
            "formats",
            "publisher_name",
            "publisher_address",
            "published_date",
            "available_copies",
            "total_copies",
            "cover_image",
        ]

    title = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={"placeholder": "Enter book title", "class": "form-control"}
        ),
        label="Title",
    )

    description = forms.CharField(
        widget=TinyMCE(attrs={"class": "form-control", "rows": 5}), label="Description"
    )

    author = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={"placeholder": "Enter author name", "class": "form-control"}
        ),
        label="Author",
    )

    genre = forms.ModelChoiceField(
        queryset=BookGenre.objects.all(),
        required=False,
        widget=forms.Select(attrs={"class": "form-control"}),
        label="Genre",
    )

    isbn = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={"placeholder": "Enter ISBN", "class": "form-control"}
        ),
        label="ISBN",
    )

    edition = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(
            attrs={"placeholder": "Enter edition (optional)", "class": "form-control"}
        ),
        label="Edition",
    )

    formats = forms.ModelMultipleChoiceField(
        queryset=BookFormat.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple(attrs={"class": "form-check-input"}),
        label="Formats",
    )

    publisher_name = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter publisher name (optional)",
                "class": "form-control",
            }
        ),
        label="Publisher Name",
    )

    publisher_address = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter publisher address (optional)",
                "class": "form-control",
            }
        ),
        label="Publisher Address",
    )

    published_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),
        label="Published Date",
    )

    available_copies = forms.IntegerField(
        min_value=0,
        initial=0,
        widget=forms.NumberInput(attrs={"class": "form-control"}),
        label="Available Copies",
    )

    total_copies = forms.IntegerField(
        min_value=1,
        widget=forms.NumberInput(attrs={"class": "form-control"}),
        label="Total Copies",
    )

    cover_image = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={"class": "form-control-file"}),
        label="Cover Image",
    )
