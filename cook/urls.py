from django.urls import path
from .views import *


app_name = 'cook'

urlpatterns = [
    path('view-orders-list/', ViewOrdersList ,name='view-orders-list'),
    path('change-order-status/<int:order_id>', ChangeOrderStatus, name='change-order-status')
]