from django import forms

from apps.core.models import Newsletter


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ["email"]

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Enter your email address"}
        ),
        help_text="We will not share your email address with anyone else.",
    )
