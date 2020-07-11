from django.db import models
from .user import Customer
from .food import Food
# Create your models here.

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    @property
    def total_cost(self):
        all_items = CartItem.objects.filter(cart=self)
        sum = 0
        for item in all_items:
            sum = sum + item.total_price
        return round(sum, 4)

    @property
    def num_of_items(self):
        return CartItem.objects.filter(cart=self).count()

    class Meta:
        verbose_name = 'Carts'
        verbose_name_plural = 'Carts'

    

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    
    @property
    def total_price(self):
        return round(self.food.price*self.quantity, 4)

    class Meta:
        verbose_name = 'CartItems'
        verbose_name_plural = 'CartItems'