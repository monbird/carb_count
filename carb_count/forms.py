from django import forms

from .models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'carbs', 'fats', 'proteins', 'calories', 'unit_name', 'unit_weight')
