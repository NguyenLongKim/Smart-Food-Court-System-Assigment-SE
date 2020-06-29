from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('paid/', views.ConfirmOrder, name='confirm_order')
]