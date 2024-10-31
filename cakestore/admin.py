from django.contrib import admin

# Register your models here.
from .models import Cart, Category, Item, Order, cartItem, orderItem

# admin.site.register(Message)
admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(orderItem)
admin.site.register(cartItem)
