from django.shortcuts import render, redirect, HttpResponse
from .cook import CookServices
# Create your views here.

def ViewOrdersList(request):
    context = {
        'orders_list' : CookServices.GetOrdersList(request.user.cook),
    }
    return render(request, 'cook/view-orders-list.html', context)

def ChangeOrderStatus(request):
    CookServices.ChangeOrderStatus(request.user.cook, request.POST.getlist('new_status'))
    return redirect('cook:view-orders-list')
