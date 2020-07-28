from django import forms

class OrderStatusForm(forms.Form):
    ORDER_STATUS_CHOICES = (
        (1, 'pending'),
        (2, 'finish'),
        (3, '<5 minutes'),
        (4, '5-10 minutes'),
    )
    status = forms.TypedChoiceField(choices=ORDER_STATUS_CHOICES)