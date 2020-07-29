from django import forms
from model.models.food import Food

class AddNewFoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ('category', 'name', 'description', 'image', 'price')