from django.contrib import admin
from .models.user import User, Customer, VendorOwner, Cook, Manager
from .models.cart import Cart, CartItem
from .models.food import Category, Food
from .models.vendor import Vendor
from .models.order import Order, OrderItem

# Register your models here.

admin.site.register(User)

admin.site.register(Customer)

admin.site.register(VendorOwner)

admin.site.register(Cook)

admin.site.register(Manager)

admin.site.register(Cart)

admin.site.register(CartItem)

admin.site.register(Category)

admin.site.register(Food)

admin.site.register(Vendor)

admin.site.register(Order)

admin.site.register(OrderItem)