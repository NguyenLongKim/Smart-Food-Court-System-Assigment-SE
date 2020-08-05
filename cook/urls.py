from django.urls import path
from .views import ViewOrdersList, ChangeOrderStatus


app_name = 'cook'

urlpatterns = [
    path('view-orders-list/', ViewOrdersList ,name='view-orders-list'),
    path('change-order-status/', ChangeOrderStatus, name='change-order-status')
]