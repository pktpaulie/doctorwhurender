# Generated by Django 4.1.7 on 2023-05-01 13:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('why_inventory', '0017_alter_inventory_quantity_sold'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='quantity_sold',
            field=models.PositiveIntegerField(blank=True, default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
