from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add_item/<int:food_id>', views.add_item_to_cart, name='add_item_to_cart'),
    path('remove_item/<int:food_id>',views.remove_item_from_cart, name='remove_item_from_cart'),
    path('update_item/<int:item_id>', views.update_quantity, name='update_quantity')
]