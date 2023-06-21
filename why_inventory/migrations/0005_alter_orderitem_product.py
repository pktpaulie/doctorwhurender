# Generated by Django 4.1.7 on 2023-04-25 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('why_inventory', '0004_alter_inventory_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orderitems', to='why_inventory.inventory'),
        ),
    ]