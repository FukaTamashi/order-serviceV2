from django.db import models
from user.validators import validate_age, validate_name


class User(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[validate_name]
    )
    email = models.EmailField(unique=True)
    age = models.IntegerField(
        validators=[validate_age]
    )

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.name
