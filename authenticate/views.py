from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from model.models.cart import Cart
from django.http import HttpResponse

# Create your views here.


def GetLogin(request):
    return render(request, 'login/index.html')


def PostLogin(request):
    inemail = request.POST.get('email')
    inpassword = request.POST.get('password')
    myuser = authenticate(username=inemail, password=inpassword)
    if (myuser is not None):
        login(request, myuser)
        if (myuser.user_type == 1):
            return redirect('customer:view-menu')
        elif (myuser.user_type == 2):
            return HttpResponse('Yay, but nothing here')
        elif (myuser.user_type == 3):
            return HttpResponse('Yay, but nothing here')
        elif (myuser.user_type == 4):
            return redirect('/admin/')
        else:
            return HttpResponse('Login failed')
    else:
        return HttpResponse('Login failed')


def LogOut(request):
    # Cart.objects.get(customer=request.user.customer).delete()
    logout(request)
    return redirect('authenticate:get_login')


def GetSignUp(request):
    return render(request, 'signup/index.html')


def PostSignUp(request):
    inusrname = request.POST.get('username')
    inpassword = request.POST.get('password')
    myuser = authenticate(username=inusrname, password=inpassword)
    if ((myuser is not None) and (myuser.user_type == 1)):
        login(request, myuser)
        return redirect('customer:view-menu')
    else:
        return HttpResponse('Login failed')


def SignUp(request):
    Cart.objects.get(customer=request.user.customer).delete()
    logout(request)
    return redirect('authenticate:get_login')
