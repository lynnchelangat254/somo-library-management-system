from django import forms

from apps.utils.constants import COUNTRIES


GENDER_CHOICES = [
    ("Female", "Female"),
    ("Male", "Male"),
]


class LoginForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(
            attrs={"placeholder": "example@example.com", "class": "form-control"}
        ),
        required=True,
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        required=True,
    )


class ResetPasswordForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(
            attrs={"placeholder": "example@example.com", "class": "form-control"}
        ),
        required=True,
    )


class MemberRequestForm(forms.Form):
    first_name = forms.CharField(
        label="First Name",
        widget=forms.TextInput(attrs={"placeholder": "John", "class": "form-control"}),
        required=True,
    )
    last_name = forms.CharField(
        label="Last Name",
        widget=forms.TextInput(attrs={"placeholder": "Doe", "class": "form-control"}),
        required=True,
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(
            attrs={"placeholder": "example@example.com", "class": "form-control"}
        ),
        required=True,
    )
    phone_number = forms.CharField(
        label="Phone Number",
        widget=forms.TextInput(
            attrs={"placeholder": "+254700000000", "class": "form-control"}
        ),
        required=True,
    )
    country = forms.ChoiceField(
        label="Country",
        choices=COUNTRIES,
        widget=forms.Select(
            attrs={"placeholder": "Choose country:", "class": "form-control"}
        ),
        required=True,
    )
    city = forms.CharField(
        label="City",
        widget=forms.TextInput(
            attrs={"placeholder": "City name", "class": "form-control"}
        ),
        required=True,
    )
    gender = forms.ChoiceField(
        label="Gender",
        choices=GENDER_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),
        required=True,
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        required=True,
    )
    confirm_password = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        required=True,
    )
