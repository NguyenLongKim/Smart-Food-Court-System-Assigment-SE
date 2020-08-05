from model.models.cart import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist

class CartManagement:
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
    def update_quantity(cart, new_quantities):
        items = CartItem.objects.filter(cart=cart)
        i=0
        for item in items:
            item.quantity = new_quantities[i]
            item.save()
            i+=1
        

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