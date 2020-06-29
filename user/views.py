from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from cart.models import Cart
# Create your views here.

class Login(View):
    def get(self, request):
        return render(request, 'login/login.html')
    def post(self, request):
        inusrname = request.POST.get('username')
        inpassword = request.POST.get('password')
        myuser = authenticate(username=inusrname, password=inpassword)
        if ( myuser != None ):
            login(request, myuser)
            return redirect('shop:food_list')
        else:
            return HttpResponse('Login failed')

def Logout(request):
    Cart.objects.get(customer=request.user).delete()
    logout(request)
    return redirect('shop:food_list')