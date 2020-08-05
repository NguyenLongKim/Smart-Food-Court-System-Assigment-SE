from django.urls import path
from .views import AddNewFood, ViewVendorsList, ViewFoodsOfVendor, EditFood, AddNewCategory, ViewStatistics

app_name = 'vendorowner'

urlpatterns = [
    path('view-vendors-list/', ViewVendorsList, name='view-vendors-list'),
    path('view-vendor-detail/<int:vendor_id>/', ViewFoodsOfVendor, name='view-vendor-detail'),
    path('edit-food/<int:vendor_id>/<int:food_id>/', EditFood, name='edit-food'),
    path('add-new-food/<int:vendor_id>/', AddNewFood ,name='add-new-food'),
    path('add-new-category/<int:vendor_id>/', AddNewCategory, name='add-new-category'),
    path('view-report/<int:vendor_id>/', ViewStatistics, name='view-statistics')
]
