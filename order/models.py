from django.db import models
from user.models import User
from user.validators import validate_order_name


class Order(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[validate_order_name]
    )
    description = models.TextField()
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)

    class Meta:
        db_table = 'order'

    def __str__(self):
        return self.name
