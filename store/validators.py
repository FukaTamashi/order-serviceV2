import re
from django.core.exceptions import ValidationError

MIN_AGE = 1
MAX_AGE = 150


def validate_name(value):
    if not re.match(r'^[A-Za-z]+$', value):
        raise ValidationError(f"{value} is not a valid name")


def validate_order_name(value):
    if not re.match(r"^[\w\s\-]+$", value):
        raise ValidationError(f"{value} is not a valid order name")


def validate_age(value):
    if value not in range(MIN_AGE, MAX_AGE + 1):
        raise ValidationError(f"{value} is not a valid age,  should be between {MIN_AGE} and {MAX_AGE}")


