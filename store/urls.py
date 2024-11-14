from django.contrib import admin
from django.urls import path
from user.views import UserAPIView
from order.views import OrderAPIView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Ручные маршруты для User
    path('api/users/', UserAPIView.as_view(), name='user-list-create'),
    path('api/users/<str:pk>/', UserAPIView.as_view(), name='user-detail-update'),

    # Ручные маршруты для Order
    path('api/orders/', OrderAPIView.as_view(), name='order-list-create'),
    path('api/orders/<str:pk>/', OrderAPIView.as_view(), name='order-detail-update'),
]

