from django import forms

from .models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'carbs', 'calories', 'fats', 'proteins', 'unit_name', 'unit_weight')
