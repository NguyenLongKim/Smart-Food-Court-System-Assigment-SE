from django.shortcuts import render, redirect
from .cook import CookServices
# Create your views here.

def ViewOrdersList(request):
    context = {
        'orders_list' : CookServices.GetOrdersList(request.user.cook),
    }
    return render(request, 'cook/view-orders-list.html', context)

def ChangeOrderStatus(request, order_id):
    CookServices.ChangeOrderStatus(order_id,request.POST.get('new_status'))
    return redirect('cook:view-orders-list')