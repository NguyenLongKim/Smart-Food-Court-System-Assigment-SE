from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist

class CartManagemnet:
    @staticmethod
    def create_cart(customer):
        return Cart.objects.create(customer=customer)

    @staticmethod
    def get_cart(customer):
        try:
            return Cart.objects.get(customer=customer)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def add_item(cart, food, quantity):
        try:
            item = CartItem.objects.get(cart=cart, food=food)
            item.quantity = item.quantity + quantity
            item.save()
        except ObjectDoesNotExist:
            CartItem.objects.create(cart=cart, food=food, quantity=quantity)
    
    @staticmethod
    def remove_item(cart, food):
        CartItem.objects.get(cart=cart, food=food).delete()

    @staticmethod
    def update_quantity(cart, item_id, new_quantity):
        item = CartItem.objects.get(cart=cart, id=item_id)
        item.quantity=new_quantity
        item.save()

    @staticmethod
    def get_all_items(cart):
        if CartItem.objects.filter(cart=cart).exists():
            return CartItem.objects.filter(cart=cart)
        else:
            return None

    @staticmethod
    def clear_cart(cart):
        all_items = CartItem.objects.filter(cart=cart)
        for item in all_items:
            item.delete()