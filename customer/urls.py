from django.urls import path
from .views import *


app_name = 'customer'

urlpatterns = [
    path('view-menu/', ViewMenu, name='view-menu'),
    path('categoies/<int:categoryID>', ViewFoodsByCategory, name='view-foods-by-category'),
    path('food_detail/<int:foodID>', ViewFoodDetail, name='view-food-detail'),
    path('view-cart/', ViewCart, name='view-cart'),
    path('add_item/<int:food_id>', AddItemToCart, name='add-item-to-cart'),
    path('remove_item/<int:food_id>', RemoveItemFromCart, name='remove-item-from-cart'),
    path('update_item/<int:item_id>', UpdateItemInCart, name='update-item-in-cart'),
    path('checkout/', Checkout, name='checkout'),
    path('submitorder/', SubmitOrder, name='submit-order'),
    path('view-orders-list/', ViewOrdersList, name='view-orders-list'),
    path('view-order-detail/<int:orderID>', ViewOrderDetail, name='view-order-detail'),
]