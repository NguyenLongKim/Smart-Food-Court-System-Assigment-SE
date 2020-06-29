from django.shortcuts import render, redirect
from shop.menu import Menu
from .CartManagement import CartManagemnet
from .forms import AddItemToCartForm
from django.http import HttpResponse

def cart_detail(request):
    cart = CartManagemnet.get_cart(customer=request.user)
    if (cart == None):
        cart = CartManagemnet.create_cart(customer=request.user)
    all_items = CartManagemnet.get_all_items(cart=cart)
    context = {
        'cart': cart,
        'all_items': all_items
    }
    return render(request, 'cart/detail.html', context)


def add_item_to_cart(request, food_id):
    form = AddItemToCartForm(request.POST)
    if form.is_valid():
        cart = CartManagemnet.get_cart(customer=request.user)
        if (cart == None):
            cart = CartManagemnet.create_cart(customer=request.user)
        food = Menu.get_food(food_id=food_id)
        CartManagemnet.add_item(cart=cart, food=food, quantity=form.cleaned_data['quantity'])
        return redirect('cart:cart_detail')

def update_quantity(request, item_id):
    cart = CartManagemnet.get_cart(customer = request.user)
    CartManagemnet.update_quantity(cart=cart, item_id=item_id, new_quantity= request.POST.get('new_quantity'))
    return redirect('cart:cart_detail')

def remove_item_from_cart(request, food_id):
    cart = CartManagemnet.get_cart(customer=request.user)
    food = Menu.get_food(food_id=food_id)
    CartManagemnet.remove_item(cart=cart, food=food)
    return redirect('cart:cart_detail')
    
