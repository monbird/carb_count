# Generated by Django 2.2.7 on 2019-11-28 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carb_count', '0008_auto_20191128_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='carbs',
            field=models.DecimalField(decimal_places=1, max_digits=5, verbose_name='Carbohydrates (g per 100g)'),
        ),
    ]
