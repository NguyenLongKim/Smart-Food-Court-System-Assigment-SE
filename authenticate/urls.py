from django.urls import path
from .views import GetLogin, PostLogin, LogOut, GetSignUp, PostSignUp

app_name = 'authenticate'

urlpatterns = [
    path('', GetLogin, name='get_login'),
    path('authenticated/', PostLogin, name='post_login'),
    path('logout/', LogOut, name='log_out'),
    path('signup/', GetSignUp, name='get_signup'),
    path('signed/', PostSignUp, name='post_signup'),
]
