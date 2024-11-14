import pytest
from rest_framework import status
from django.urls import reverse
from user.models import User
from order.models import Order


@pytest.fixture
def user():
    user = User(
        name='testuser',
        email='test@gmail.com',
        age=52
    )
    user.save()
    return user


@pytest.fixture
def order_data(user):
    return {
        "name": "Boots",
        "description": "Leather boots",
        "user": user
    }


@pytest.fixture
def create_order(order_data):
    return Order.objects.create(**order_data)


@pytest.mark.django_db
def test_create_order(client, order_data, user):
    url = reverse('order-list')
    order_data['user'] = user.id

    response = client.post(url, order_data, content_type='application/json')

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['name'] == order_data['name']
    assert response.data['description'] == order_data['description']
    assert response.data['user'] == order_data['user']



@pytest.mark.django_db
def test_update_order_put(client, create_order, user):
    url = reverse('order-detail', args=[create_order.id])
    updated_data = {
        "name": "Updated Boots",
        "description": "Updated leather boots",
        "user": user.id
    }

    response = client.put(url, updated_data, content_type='application/json')

    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == updated_data['name']
    assert response.data['description'] == updated_data['description']
    assert response.data['user'] == updated_data['user']


@pytest.mark.django_db
def test_update_order_patch(client, create_order):
    url = reverse('order-detail', args=[create_order.id])
    updated_data = {
        "description": "Partially updated description"
    }

    response = client.patch(url, updated_data, content_type='application/json')

    assert response.status_code == status.HTTP_200_OK
    assert response.data['description'] == updated_data['description']
    assert response.data['name'] == create_order.name
    assert response.data['user'] == create_order.user.id
