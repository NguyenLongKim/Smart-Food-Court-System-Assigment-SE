from django.shortcuts import render, redirect
from .cook import CookServices
from .forms import OrderStatusForm
# Create your views here.

def ViewOrdersList(request):
    orders_list = CookServices.GetOrdersList(request.user.cook)
    change_status_forms = {}
    for item in orders_list:
        change_status_forms[item.food.name]=OrderStatusForm(initial={'status': item.status})
    context = {
        'orders_list' : orders_list,
        'change_status_forms' : OrderStatusForm()
    }
    return render(request, 'cook/view-orders-list.html', context)

def ChangeOrderStatus(request, order_id):
    CookServices.ChangeOrderStatus(order_id,request.POST.get('new_status'))
    return redirect('cook:view-orders-list')