from django.db import models
from user.models import CustomerUser
from shop.models import Food
from cart.CartManagement import CartManagemnet
# Create your models here.

class Order(models.Model):
    customer = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @staticmethod
    def create_order(customer):
        order = Order.objects.create(customer=customer)
        cart = CartManagemnet.get_cart(customer=customer)
        all_cart_items = CartManagemnet.get_all_items(cart=cart)
        for item in all_cart_items:
            OrderItem.objects.create(order=order, food = item.food, quantity = item.quantity)
        CartManagemnet.clear_cart(cart=cart)
        return order
    
    def __str__(self):
        return self.customer.username + "'s order"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Item: ' + self.food.name + ' in ' + self.order.customer.username + "'s order"
