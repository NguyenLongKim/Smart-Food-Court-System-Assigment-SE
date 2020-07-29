from django.shortcuts import render, redirect, HttpResponse
from .forms import AddNewFoodForm
from .vendorowner import VendorOwnerServices
from model.models.food import Food 
# Create your views here.

def AddNewFood(request, vendor_id):
    if request.method == 'GET':
        context = {
            'add_new_food_form' : AddNewFoodForm()
        }
        return render(request, 'vendorowner/add-new-food.html', context)
    elif request.method == 'POST':
        new_food_form = AddNewFoodForm(request.POST, request.FILES)
        VendorOwnerServices.AddFood(vendor_id, new_food_form)
        return redirect('vendorowner:view-vendor-detail', vendor_id = vendor_id)

def ViewVendorsList(request):
    context = {
        'vendors' : VendorOwnerServices.GetVendorList(request.user.vendorowner)
    }
    return render(request, 'vendorowner/vendors-list.html', context)

def ViewFoodsOfVendor(request, vendor_id):
    context = {
        'vendor_id': vendor_id,
        'foods' : VendorOwnerServices.GetFoodsList(vendor_id)
    }
    return render(request, 'vendorowner/vendor-detail.html', context)

def EditFood(request, vendor_id, food_id):
    if request.method == 'GET':
        food = Food.objects.get(id=food_id)
        context = {
            'edit_food_form' : AddNewFoodForm(initial={'category' : food.category, 'name': food.name, 'description': food.description, 'image': food.image, 'price': food.price})
        }
        return render(request, 'vendorowner/edit-food.html', context)
    elif request.method == 'POST':
        if (request.POST['edit-food-action'] == 'Update'):
            update_form = AddNewFoodForm(request.POST, request.FILES)
            if update_form.is_valid():
                VendorOwnerServices.UpdateFood(food_id,update_form)
                return redirect('vendorowner:view-vendor-detail', vendor_id = vendor_id)
        elif (request.POST['edit-food-action'] == 'Delete'):
            VendorOwnerServices.RemoveFood(food_id)
            return redirect('vendorowner:view-vendor-detail', vendor_id = vendor_id)
        
        


