from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from model.models.cart import Cart
from django.http import HttpResponse

# Create your views here.

def GetLogin(request):
    return render(request, 'login/index.html')

def PostLogin(request):
    inusrname = request.POST.get('username')
    inpassword = request.POST.get('password')
    myuser = authenticate(username=inusrname, password=inpassword)
    if ( (myuser != None) and (myuser.type_account=='customer') ):
        login(request, myuser)
        return redirect('customer:view-menu')
    elif ( (myuser != None) and (myuser.type_account=='cook') ):
        login(request, myuser)
        return redirect('cook:view-orders-list')
    elif ( (myuser != None) and (myuser.type_account=='vendorowner') ):
        login(request, myuser)
        return redirect('vendorowner:view-vendors-list')
    else:
        return HttpResponse('Login failed')

def LogOut(request):
    if (request.user.type_account=='customer'):
        Cart.objects.get(customer=request.user.customer).delete()
    logout(request)
    return redirect('authenticate:get_login')