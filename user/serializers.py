from rest_framework import serializers

from store.validators import validate_user_exists
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'age']


