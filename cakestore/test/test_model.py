import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from cakestore.models import Category, Item, Cart, cartItem, Order, orderItem


@pytest.mark.django_db  # Use this marker to allow database access for the test
class TestModels:

    def test_category_creation(self):
        category = Category.objects.create(name="Cake")
        assert category.name == "Cake"
        assert str(category) == "Cake"

    def test_item_creation(self):
        category = Category.objects.create(name="Cake")
        item = Item.objects.create(
            name="Chocolate Cake",
            category=category,
            price=10.00,
            description="Delicious chocolate cake",
        )

        assert item.name == "Chocolate Cake"
        assert item.category == category
        assert item.price == 10.00
        assert str(item) == "Chocolate Cake"

    def test_cart_creation(self):
        category = Category.objects.create(name="Cake")
        item = Item.objects.create(
            name="Chocolate Cake", category=category, price=10.00
        )
        cart = Cart.objects.create(item=item, quantity=2)

        assert cart.item == item
        assert cart.quantity == 2
        assert cart.total_ordering == 0  # Check initial default value
        assert str(cart) == "Chocolate Cake"

    def test_cart_total_ordering(self):
        category = Category.objects.create(name="Cake")
        item = Item.objects.create(
            name="Chocolate Cake", category=category, price=10.00
        )
        cart = Cart.objects.create(item=item, quantity=3)

        assert cart.total_odering == 30.00  # 3 * 10.00 = 30.00
        cart.save()
        assert cart.total_ordering == 30.00  # Ensure total_ordering is saved correctly

    def test_cart_item_creation(self):
        category = Category.objects.create(name="Cake")
        item = Item.objects.create(
            name="Chocolate Cake", category=category, price=10.00
        )
        cart = Cart.objects.create(item=item, quantity=2)
        cart_item = cartItem.objects.create(cart=cart, item=item, quantity=1)

        assert cart_item.cart == cart
        assert cart_item.item == item
        assert cart_item.quantity == 1
        assert str(cart_item) == "Chocolate Cake"

    def test_order_creation(self):
        user = User.objects.create_user(username="testuser", password="testpassword")
        category = Category.objects.create(name="Cake")
        item = Item.objects.create(
            name="Chocolate Cake", category=category, price=10.00
        )
        order = Order.objects.create(User=user, item=item, quantity=2)

        assert order.User == user
        assert order.item == item
        assert order.quantity == 2
        assert order.status == "Pending"
        assert order.total_ordering == 0  # Check initial default value

    # def test_order_total_ordering(self):
    #    user = User.objects.create_user(username='testuser', password='testpassword')
    #    category = Category.objects.create(name='Cake')
    #    item = Item.objects.create(name='Chocolate Cake', category=category, price=10.00)
    # order = Order.objects.create(User=user, item=item, quantity=3)

    # assert order.total_odering == 30.00  # 3 * 10.00 = 30.00
    # order.save()
    # assert order.total_ordering == 30.00  # Ensure total_ordering is saved correctly
    # def test_order_total_ordering(self):
    #  user = User.objects.create_user(username='testuser', password='testpassword')
    # category = Category.objects.create(name='Cake')
    # item = Item.objects.create(name='Chocolate Cake', category=category, price=10.00)
    # order = Order.objects.create(User=user, item=item, quantity=3)

    # assert order.total_odering == 30.00  # 3 * 10.00 = 30.00

    def test_order_item_creation(self):
        user = User.objects.create_user(username="testuser", password="testpassword")
        category = Category.objects.create(name="Cake")
        item = Item.objects.create(
            name="Chocolate Cake", category=category, price=10.00
        )
        order = Order.objects.create(User=user, item=item, quantity=1)
        order_item = orderItem.objects.create(order=order, item=item, quantity=1)

        assert order_item.order == order
        assert order_item.item == item
        assert order_item.quantity == 1
        assert str(order_item) == "Chocolate Cake"
