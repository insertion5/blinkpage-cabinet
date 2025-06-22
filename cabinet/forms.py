from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['site_type', 'services', 'total_price']
        widgets = {
            'services': forms.CheckboxSelectMultiple,
        }
