from django.db import models
from user.models import CustomerUser
from shop.models import Food

# Create your models here.

class Cart(models.Model):
    customer = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)

    @property
    def get_total_cost(self):
        all_items = CartItem.objects.filter(cart=self)
        sum = 0
        for item in all_items:
            sum = sum + item.get_price
        return sum

    def __str__(self):
        return self.customer.username + "'s cart" 


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    @property
    def get_price(self):
        return self.food.price*self.quantity

    def __str__(self):
        return 'Item: ' + self.food.name + ' in ' + self.cart.customer.username + "'s cart"



    
    
