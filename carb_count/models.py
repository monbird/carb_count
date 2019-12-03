from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, null=False)
    carbs = models.DecimalField(max_digits=5, decimal_places=1, null=False, verbose_name='Carbohydrates (g per 100g)')
    calories = models.DecimalField(max_digits=5, decimal_places=1, null=False, verbose_name='Energy (kcal per 100g)')
    fats = models.DecimalField(max_digits=5, decimal_places=1, null=False, verbose_name='Fat (g per 100g)')
    proteins = models.DecimalField(max_digits=5, decimal_places=1, null=False, verbose_name='Protein (g per 100g)')
    unit_name = models.CharField(max_length=50, null=False)
    unit_weight = models.DecimalField(max_digits=5, decimal_places=1, null=False, verbose_name='Unit weight (g)')
    add_to_meal = models.BooleanField(default=False, null=False)

    def __str__(self):
        return self.name
