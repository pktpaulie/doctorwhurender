# Generated by Django 4.1.7 on 2023-05-02 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('why_inventory', '0032_remove_cart_product_cart_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='product',
        ),
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ManyToManyField(to='why_inventory.inventory'),
        ),
    ]
