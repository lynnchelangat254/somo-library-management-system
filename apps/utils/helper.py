from string import ascii_letters
import random


def generate_password() -> str:
    values = ascii_letters + "0123456789" + ".+()&$#@%![]"
    return str(random.choices([val for val in values], k=8))
