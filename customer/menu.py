from model.models.food import Category, Food
from model.models.vendor import Vendor
from django.core.exceptions import ObjectDoesNotExist

class Menu:
    @staticmethod
    def get_all_categories():
        if Category.objects.exists():
            return Category.objects.all()
        else:
            return None

    @staticmethod
    def get_category(cat_id):
        try:
            return Category.objects.get(id=cat_id)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def get_all_vendors():
        if Vendor.objects.exists():
            return Vendor.objects.all()
        else:
            return None

    @staticmethod
    def get_vendor(ven_id):
        try:
            return Vendor.objects.get(id=ven_id)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def get_all_foods():
        if Food.objects.exists():
            return Food.objects.all()
        else:
            return None

    @staticmethod
    def get_list_foods_by_category(category):
        if Food.objects.filter(category=category).exists():
            return Food.objects.filter(category=category)
        else:
            return None

    @staticmethod
    def get_list_foods_by_vendor(vendor):
        if Food.objects.filter(vendor=vendor).exists():
            return Food.objects.filter(vendor=vendor)
        else:
            return None

    @staticmethod
    def get_food(food_id):
        try:
            return Food.objects.get(id=food_id)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def Search(food_name):
        foods = Food.objects.all()
        rt = []
        for food in foods:
            if (food_name.lower() in food.name.lower() or food.name.lower() in food_name.lower()):
                rt.append(food)
        if not rt:
            return None
        else:
            return rt
