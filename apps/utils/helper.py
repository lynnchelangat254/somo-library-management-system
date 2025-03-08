from string import ascii_letters
import random
import re

from django.core.exceptions import ValidationError


def generate_password() -> str:
    values = ascii_letters + "0123456789" + ".+()&$#@%![]"
    return str(random.choices([val for val in values], k=8))


def validate_phone_number(value):
    phone_regex = re.compile(r"^\+?1?\d{9,15}$")  # International phone format
    if not phone_regex.match(value):
        raise ValidationError("Enter a valid phone number.")
