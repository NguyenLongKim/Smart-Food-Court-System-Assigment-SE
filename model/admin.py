from django.contrib import admin
# from .models.cart import Cart, CartItem
from .models.food import Category, Food
from .models.vendor import Vendor
from .models.order import Order, OrderItem, OrdersLog
# from .models.order import Order, OrderItem


# Register your models here.

# admin.site.register(Cart)

# admin.site.register(CartItem)

admin.site.register(Category)

admin.site.register(Food)

admin.site.register(Vendor)

admin.site.register(Order)

admin.site.register(OrderItem)

admin.site.register(OrdersLog)

# admin.site.register(OrderItem)

