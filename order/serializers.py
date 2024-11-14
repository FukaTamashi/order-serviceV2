from rest_framework import serializers

from store.validators import validate_user_exists
from user.models import User
from .models import Order


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'

