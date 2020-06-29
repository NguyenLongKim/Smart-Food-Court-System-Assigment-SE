from django.shortcuts import render, redirect
from cart.CartManagement import CartManagemnet
from .models import Order

def checkout(request):
    cart = CartManagemnet.get_cart(customer=request.user)
    all_items = CartManagemnet.get_all_items(cart=cart)
    context = {
        'cart': cart,
        'all_items': all_items
    }
    return render(request, 'order/checkout.html', context)

def ConfirmOrder(request):
    order = Order.create_order(customer=request.user)
    context = {
        'order': order
    }
    return render(request, 'order/created.html', context)