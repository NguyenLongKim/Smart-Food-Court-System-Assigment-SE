from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.food_list, name='food_list'),
    path('categoies/<int:categoryID>', views.food_list_by_category, name='food_list_by_category'),
    path('food_detail/<int:foodID>', views.food_detail, name='food_detail')
]
