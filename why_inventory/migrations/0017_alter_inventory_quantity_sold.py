# Generated by Django 4.1.7 on 2023-05-01 13:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('why_inventory', '0016_alter_inventory_cost_per_item_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='quantity_sold',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
