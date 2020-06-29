from django.shortcuts import render
from django.http import HttpResponse
from .menu import Menu
from cart.forms import AddItemToCartForm

def food_list(request):
    context = {
        'category': None,
        'categories': Menu.get_all_categories(),
        'foods': Menu.get_all_foods(),
    }
    return render(request, 'food/list.html', context)

def food_list_by_category(request, categoryID=None):
    context = {
        'category': Menu.get_category(cat_id=categoryID),
        'categories': Menu.get_all_categories(),
        'foods': Menu.get_list_foods_by_category(category=Menu.get_category(cat_id=categoryID)),
    }
    return render(request, 'food/list.html', context)

def food_detail(request, foodID=None):
    context = {
        'food': Menu.get_food(food_id=foodID),
        'add_item_to_cart_form': AddItemToCartForm()
    }
    return render(request, 'food/detail.html', context)