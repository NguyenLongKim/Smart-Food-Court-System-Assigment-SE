from model.models.order import Order, OrderItem, OrdersLog
from model.models.cart import Cart
from model.models.user import Customer
from .cart import CartManagement
from django.core.exceptions import ObjectDoesNotExist

import datetime


# Create your models here.

class OrderManagement():
    @staticmethod
    def create_order(customer):
        cart = CartManagement.get_cart(customer=customer)
        if (cart.total_cost <= customer.balance):
            customer.balance-=cart.total_cost
            customer.save()
            order = Order.objects.create(customer=customer, created=datetime.datetime.now())      
            all_cart_items = CartManagement.get_all_items(cart=cart)
            for item in all_cart_items:
                OrderItem.objects.create(order=order, food = item.food, quantity = item.quantity, created=datetime.datetime.now())
            OrdersLogManagement.add_new_order(all_cart_items)
            CartManagement.clear_cart(cart=cart)
            return order
        else:
            return None
    
    @staticmethod
    def get_orders_list(customer):
        orders = list(Order.objects.filter(customer=customer))
        orders.reverse()
        return orders

    @staticmethod
    def get_items_of_order(order_id):
        return OrderItem.objects.filter(order=Order.objects.get(id=order_id))


class OrdersLogManagement():
    @staticmethod
    def add_new_order(items):
        for item in items:
            try:
                obj = OrdersLog.objects.get(food=item.food)
                obj.quantity+=item.quantity
                obj.save()
            except ObjectDoesNotExist:
                OrdersLog.objects.create(food=item.food, vendor=item.food.vendor, quantity=item.quantity)

    
