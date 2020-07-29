from model.models.user import VendorOwner
from model.models.vendor import Vendor
from model.models.food import  Food

class VendorOwnerServices:
    @staticmethod
    def GetVendorList(owner):
        return Vendor.objects.filter(owner=owner)

    @staticmethod
    def GetFoodsList(vendor_id):
        vendor = Vendor.objects.get(id=vendor_id)
        return Food.objects.filter(vendor=vendor)

    @staticmethod
    def RemoveFood(food_id):
        Food.objects.get(id=food_id).delete()

    @staticmethod
    def UpdateFood(food_id, update_form):
        food = Food.objects.get(id=food_id)
        food.category = update_form.cleaned_data['category']
        food.name = update_form.cleaned_data['name']
        food.price = update_form.cleaned_data['price']
        food.image = update_form.cleaned_data['image']
        food.description = update_form.cleaned_data['description']
        food.save()

    @staticmethod
    def AddFood(vendor_id, new_food_form):
        if new_food_form.is_valid():
            food = Food.objects.create(category=new_food_form.cleaned_data['category'], vendor=Vendor.objects.get(id=vendor_id))
            food.name = new_food_form.cleaned_data['name']
            food.price = new_food_form.cleaned_data['price']
            food.image = new_food_form.cleaned_data['image']
            food.description = new_food_form.cleaned_data['description']
            food.save()

