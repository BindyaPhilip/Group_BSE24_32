# cakestore/tests/test_integration.py

import pytest
from django.contrib.auth.models import User
from django.urls import reverse

from cakestore.models import Cart, Category, Item


@pytest.mark.django_db  # This decorator allows the test to access the database
class TestIntegration:

    @pytest.fixture
    def user(self):
        """Create a test user."""
        user = User.objects.create_user(username="testuser", password="12345")
        return user

    @pytest.fixture
    def category(self):
        """Create a test category."""
        category = Category.objects.create(name="Cakes")
        return category

    @pytest.fixture
    def item(self, category):
        """Create a test item."""
        item = Item.objects.create(name="Cheesecake", category=category, price=7000)
        return item

    @pytest.fixture
    def cart(self, item):
        """Create a test cart with an item."""
        cart = Cart.objects.create(item=item, quantity=2)
        return cart

    # def test_checkout_view(self, client, user, cart):
    #     """Test the checkout view."""
    #     # Log in the user
    #     client.login(username='testuser', password='12345')

    #     # Simulate a GET request to the checkout view
    #     response = client.get(reverse('checkout'))

    #     # Check if the checkout page is rendered with the cart and total
    #     assert response.status_code == 200
    #     assert 'cart' in response.context
    #     assert response.context['total'] == cart.quantity * cart.item.price  # Check the total

    def test_cart_creation(self, item):
        """Test if cart can be created correctly."""
        cart = Cart.objects.create(item=item, quantity=3)
        assert cart.id is not None  # Check if cart is created
        assert cart.quantity == 3  # Check the quantity
        assert cart.item == item  # Check the associated item
