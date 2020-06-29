from django import forms


class AddItemToCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1,max_value=100)
