from django.db import models
from .user import Customer
from .food import Food
# Create your models here.

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created = models.DateTimeField()

    class Meta:
        verbose_name = 'Orders'
        verbose_name_plural = 'Orders'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    created = models.DateTimeField()
    status = models.CharField(max_length=50, default='pending')

    class Meta:
        verbose_name = 'OrderItems'
        verbose_name_plural = 'OrderItems'