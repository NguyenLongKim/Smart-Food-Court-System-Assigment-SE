from .models import Food, Category
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
    def get_food(food_id):
        try:
            return Food.objects.get(id=food_id)
        except ObjectDoesNotExist:
            return None
