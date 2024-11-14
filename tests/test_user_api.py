import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from user.models import User
from order.models import Order
import uuid

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user():
    return User.objects.create(
        id=uuid.uuid4(),
        name="Test User",
        email="testuser@example.com",
        age=25
    )

@pytest.fixture
def order(user):
    return Order.objects.create(
        id=uuid.uuid4(),
        name="Test Order",
        description="This is a test order",
        user=user
    )

@pytest.fixture
def order_data(user):
    return {
        "name": "New Test Order",
        "description": "This is a new test order",
        "user": str(user.id)
    }

@pytest.mark.django_db
def test_get_orders(api_client, order):
    url = reverse('order-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) > 0

@pytest.mark.django_db
def test_create_order(api_client, user, order_data):
    url = reverse('order-list')
    response = api_client.post(url, order_data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['name'] == order_data['name']
    assert response.data['description'] == order_data['description']
    assert response.data['user'] == user.id

@pytest.mark.django_db
def test_update_order(api_client, order, user):
    url = reverse('order-detail', args=[order.id])
    updated_data = {
        "name": "Updated Order",
        "description": "Updated description",
        "user": str(user.id)
    }
    response = api_client.put(url, updated_data, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == updated_data['name']
    assert response.data['description'] == updated_data['description']

@pytest.mark.django_db
def test_partial_update_order(api_client, order):
    url = reverse('order-detail', args=[order.id])
    updated_data = {
        "description": "Partially updated description"
    }
    response = api_client.patch(url, updated_data, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['description'] == updated_data['description']
