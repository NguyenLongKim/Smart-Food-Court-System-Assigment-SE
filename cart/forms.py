from django import forms


class AddItemToCartForm(forms.Form):
    quantity = forms.IntegerField()
