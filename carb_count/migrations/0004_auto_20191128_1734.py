# Generated by Django 2.2.7 on 2019-11-28 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carb_count', '0003_product_add_to_meal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='calories',
            field=models.DecimalField(decimal_places=1, max_digits=5, verbose_name='Energy (kcal in 100g of product)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='carbs',
            field=models.DecimalField(decimal_places=1, max_digits=5, verbose_name='Carbs (g in 100g of product)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='fats',
            field=models.DecimalField(decimal_places=1, max_digits=5, verbose_name='Fats (g in 100g of product)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='proteins',
            field=models.DecimalField(decimal_places=1, max_digits=5, verbose_name='Proteins (g in 100g of product)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='unit_weight',
            field=models.DecimalField(decimal_places=1, max_digits=5, verbose_name='Unit weight (g)'),
        ),
    ]
