import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client
from cakestore.models import Item, Cart, Category, Order, orderItem
from django.db.models import Sum
from django.core.files.uploadedfile import SimpleUploadedFile


# Use the pytest fixture to create a test client for making HTTP requests
@pytest.fixture
def client():
    return Client()


# Test the home page view
@pytest.mark.django_db
def test_show_home(client):
    # Create some items and a cart
    category = Category.objects.create(name="Cakes")
    item = Item.objects.create(name="Chocolate Cake", category=category, price=5000)
    Cart.objects.create(item=item, quantity=2)

    # Simulate an HTTP GET request to the home view
    response = client.get(reverse("home"))

    # Check if the response is OK (status code 200)
    assert response.status_code == 200

    # Verify that the context contains 'items' and 'cart'
    assert "items" in response.context
    assert "cart" in response.context

    # Verify that the quantity sum is correctly calculated
    assert response.context["quantity"] == 2


# Test adding an item to the cart
@pytest.mark.django_db
def test_add_to_cart(client):
    category = Category.objects.create(name="Cakes")
    item = Item.objects.create(name="Vanilla Cake", category=category, price=1000)

    # Simulate an HTTP GET request to add an item to the cart
    response = client.get(reverse("addCart", args=[item.id]))

    # Check if the item has been added to the cart
    cart = Cart.objects.filter(item=item).first()
    assert cart is not None
    assert cart.quantity == 1

    # Verify that after adding, the user is redirected to the menu
    assert response.status_code == 302
    assert response.url == reverse("menu")


# Test displaying the cart
@pytest.mark.django_db
def test_display_cart(client):
    category = Category.objects.create(name="Cakes")
    image_file = SimpleUploadedFile(
        name="test_image.jpg", content=b"", content_type="image/jpeg"
    )
    item = Item.objects.create(
        name="Chocolate Cake", category=category, price=5000, image=image_file
    )
    cart = Cart.objects.create(item=item, quantity=3)

    # Simulate a GET request to the cart display view
    response = client.get(reverse("Cart"))
    assert response.status_code == 200


# @pytest.mark.django_db
# def test_display_cart(client):
# category = Category.objects.create(name='Cakes')
# item = Item.objects.create(name='Chocolate Cake', category=category, price=5000)
# cart = Cart.objects.create(item=item, quantity=3)

# Simulate a GET request to the cart display view
# response = client.get(reverse('Cart'))

# Check if the cart is displayed with the correct data
# assert response.status_code == 200
# assert 'cart' in response.context
# assert 'total' in response.context
# assert response.context['total'] == cart.quantity * item.price

# Test the checkout page (user login required)
# @pytest.mark.django_db
# def test_checkout_view(client):
# user = User.objects.create_user(username='testuser', password='12345')
# client.login(username='testuser', password='12345')

# category = Category.objects.create(name='Cakes')
# item = Item.objects.create(name='Cheesecake', category=category, price=7000)
# Cart.objects.create(item=item, quantity=2)

# Simulate a GET request to the checkout view
# response = client.get(reverse('checkout'))

# Check if the checkout page is rendered with the cart and total
# assert response.status_code == 200
# assert 'cart' in response.context
# assert response.context['total'] == 2 * item.price


# Test creating an order (cash on delivery)
@pytest.mark.django_db
def test_cash_on_delivery(client):
    user = User.objects.create_user(username="testuser", password="12345")
    client.login(username="testuser", password="12345")

    category = Category.objects.create(name="Cakes")
    item = Item.objects.create(name="Red Velvet Cake", category=category, price=15000)
    Cart.objects.create(item=item, quantity=1)

    # Simulate a POST request to place the order
    response = client.post(reverse("cash_on_delivery"))

    # Check if an order has been created and cart is cleared
    order = Order.objects.filter(User=user).first()
    assert order is not None
    assert order.item == item
    assert order.quantity == 1

    # Verify that the cart has been cleared
    assert Cart.objects.count() == 0
    assert response.status_code == 200


# Test user login functionality
@pytest.mark.django_db
def test_login_user(client):
    # Create a user
    user = User.objects.create_user(username="testuser", password="12345")

    # Simulate a POST request to log in
    response = client.post(
        reverse("login"),
        {
            "username": "testuser",
            "password": "12345",
        },
    )

    # Check if the user is logged in and redirected to the home page
    assert response.status_code == 302
    assert response.url == reverse("home")
