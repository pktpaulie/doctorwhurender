# Generated by Django 4.1.7 on 2023-05-01 11:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('why_inventory', '0012_rename_items_cart_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='minimum_stock_level',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]