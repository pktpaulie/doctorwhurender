# Generated by Django 4.1.7 on 2023-05-01 14:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('why_inventory', '0024_alter_inventory_name_alter_inventory_sales'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='quantity_in_stock',
            field=models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
