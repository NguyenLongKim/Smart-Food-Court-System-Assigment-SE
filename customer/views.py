from django.shortcuts import render, redirect
from model.models.food import Category, Food
from model.models.vendor import Vendor
from model.models.cart import Cart
from model.models.user import User, Customer, VendorOwner
from .menu import Menu
from .cart import CartManagement
from .order import OrderManagement
from django.http import HttpResponse
# Create your views here.
    
def ViewMenu(request):
    context = {
        'categories': Menu.get_all_categories,
        'vendors': Menu.get_all_vendors(),
        'foods': Menu.get_all_foods()
    }
    return render(request, 'order/shop-grid.html', context)

def ViewFoodsByCategory(request, categoryID=None):
    context = {
        'category': Menu.get_category(cat_id=categoryID),
        'categories': Menu.get_all_categories(),
        'vendors': Menu.get_all_vendors(),
        'foods': Menu.get_list_foods_by_category(category=Menu.get_category(cat_id=categoryID)),  
    }
    return render(request, 'order/shop-grid.html', context)

def ViewFoodsByVendor(request, vendorID=None):
    context = {
        'vendor': Menu.get_vendor(vendorID),
        'categories': Menu.get_all_categories(),
        'vendors': Menu.get_all_vendors(),
        'foods': Menu.get_list_foods_by_vendor(vendor=Menu.get_vendor(vendorID)),
    }
    return render(request, 'order/shop-grid.html', context)

def ViewBySearch(request):
    context = {
        'categories': Menu.get_all_categories(),
        'vendors': Menu.get_all_vendors(),
        'foods': Menu.Search(food_name=request.POST['food_name']),
        'search' : True,
    }
    return render(request, 'order/shop-grid.html', context)

def ViewFoodDetail(request, foodID=None):
    context = {
        'food': Menu.get_food(food_id=foodID),
    }
    return render(request, 'order/shop-details.html', context)

def ViewCart(request):
    cart = CartManagement.get_cart(customer=request.user.customer)
    if (cart == None):
        cart = CartManagement.create_cart(customer=request.user.customer)
    context = {
        'cart': cart,
        'all_items': CartManagement.get_all_items(cart=cart)
    }
    return render(request, 'order/shoping-cart.html', context)

def AddItemToCart(request, food_id):
    cart = CartManagement.get_cart(customer=request.user.customer)
    if (cart == None):
        cart = CartManagement.create_cart(customer=request.user.customer)
    food = Menu.get_food(food_id=food_id)
    CartManagement.add_item(cart=cart, food=food, quantity=int(request.POST.get("quantity")))
    return redirect('customer:view-cart')

def RemoveItemFromCart(request, food_id):
    cart = CartManagement.get_cart(customer=request.user.customer)
    food = Menu.get_food(food_id=food_id)
    CartManagement.remove_item(cart=cart, food=food)
    return redirect('customer:view-cart')

def UpdateItemInCart(request, item_id):
    cart = CartManagement.get_cart(customer = request.user.customer)
    CartManagement.update_quantity(cart=cart, item_id=item_id, new_quantity= int(request.POST.get('new_quantity')))
    return redirect('customer:view-cart')

def Checkout(request):
    cart = CartManagement.get_cart(customer=request.user.customer)
    if (cart == None):
        cart = CartManagement.create_cart(customer=request.user.customer)
    context = {
        'cart': cart,
        'all_items': CartManagement.get_all_items(cart=cart)
    }
    return render(request, 'order/checkout.html', context)

def SubmitOrder(request):
    context = {
        'order_result' : OrderManagement.create_order(customer=request.user.customer)
    }
    return render(request, 'order/order-result.html', context)

def ViewOrdersList(request):
    context = {
        'orders': OrderManagement.get_orders_list(customer=request.user.customer)
    }
    return render(request, 'order/view-orders-list.html', context)

def ViewOrderDetail(request, orderID):
    context = {
        'items': OrderManagement.get_items_of_order(orderID)
    }
    return render(request, 'order/view-order-detail.html', context)