from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from model.models.cart import Cart
from django.http import HttpResponse
from model.models import user

User = get_user_model()
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
    """
    try:
        inemail = request.POST.get('email')
    except ValueError:
        # if inemail is None:
        return render(request, 'signup/index.html', {'email_error': 'Email is required'})
    """

    inemail = request.POST.get('email')
    if inemail == "":
        return render(request, 'signup/index.html', {'email_error': 'Email is required'})

    qs = User.objects.filter(email=inemail)
    if qs.exists():
        return render(request, 'signup/index.html', {'email_error': 'Email is taken'})

    inpassword = request.POST.get('password')
    if inpassword == "":
        return render(request, 'signup/index.html', {'password_error': 'Password is required'})

    inDoB = request.POST.get('date_of_birth')
    if inDoB == "":
        return render(request, 'signup/index.html', {'bd_error': 'Birth day is required'})

    newuser = User.objects.create_user(
        email=inemail,
        date_of_birth=inDoB,
        user_type=1,
        password=inpassword,
    )
    if (newuser is not None):
        return render(request, 'signup/signed.html')
    else:
        return HttpResponse('Sign up failed')
