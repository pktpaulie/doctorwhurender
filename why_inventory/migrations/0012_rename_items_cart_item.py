# Generated by Django 4.1.7 on 2023-05-01 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('why_inventory', '0011_alter_cartitem_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='items',
            new_name='item',
        ),
    ]