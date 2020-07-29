from django.urls import path
from .views import AddNewFood, ViewVendorsList, ViewFoodsOfVendor, EditFood

app_name = 'vendorowner'

urlpatterns = [
    path('view-vendors-list/', ViewVendorsList, name='view-vendors-list'),
    path('view-vendor-detail/<int:vendor_id>', ViewFoodsOfVendor, name='view-vendor-detail'),
    path('edit-food/<int:vendor_id>/<int:food_id>', EditFood, name='edit-food'),
    path('add-new-food/<int:vendor_id>', AddNewFood ,name='add-new-food'),
]
