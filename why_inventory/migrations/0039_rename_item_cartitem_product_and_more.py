# Generated by Django 4.1.7 on 2023-05-04 05:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('why_inventory', '0038_alter_inventory_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='item',
            new_name='product',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='customer_name',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='paid_amount',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='product',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='complete',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='sold_item',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='sold_quantity',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='unit_price',
        ),
        migrations.AddField(
            model_name='sale',
            name='cost_per_item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='why_inventory.inventory'),
        ),
        migrations.AddField(
            model_name='sale',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='why_inventory.cartitem'),
        ),
    ]
