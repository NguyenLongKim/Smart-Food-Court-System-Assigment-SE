from django.db import models
from .user import Customer
from .food import Food
# Create your models here.


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created = models.DateTimeField()

    @property
    def total_cost(self):
        all_items = OrderItem.objects.filter(order=self)
        sum = 0
        for item in all_items:
            sum = sum + item.total_price
        return round(sum, 4)

    @property
    def num_of_items(self):
        return OrderItem.objects.filter(order=self).count()

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    created = models.DateTimeField()
    status = models.CharField(max_length=50, default='pending')

    @property
    def total_price(self):
        return round(self.food.price * self.quantity, 4)

    class Meta:
        verbose_name = 'OrderItem'
        verbose_name_plural = 'OrderItems'
