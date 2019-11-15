from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, null=False)
    carbs = models.DecimalField(max_digits=5, decimal_places=1, null=False)
    fats = models.DecimalField(max_digits=5, decimal_places=1, null=False)
    proteins = models.DecimalField(max_digits=5, decimal_places=1, null=False)
    calories = models.DecimalField(max_digits=5, decimal_places=1, null=False)
    unit_name = models.CharField(max_length=50, null=False)
    unit_weight = models.DecimalField(max_digits=5, decimal_places=1, null=False)

    def __str__(self):
        return self.name
