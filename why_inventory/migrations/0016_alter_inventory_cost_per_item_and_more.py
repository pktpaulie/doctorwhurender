# Generated by Django 4.1.7 on 2023-05-01 13:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('why_inventory', '0015_cartitem_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='cost_per_item',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='quantity_sold',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
