# Generated by Django 4.1.7 on 2023-05-01 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('why_inventory', '0026_alter_inventory_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='minimum_stock_level',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
