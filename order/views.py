from rest_framework import viewsets, status
from rest_framework.response import Response

from user.models import User
from .models import Order
from .serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    http_method_names = ['get', 'post', 'put', 'patch']

    def perform_create(self, serializer):
        user_id = self.request.data.get('user')
        serializer.save()
