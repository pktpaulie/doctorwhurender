# Generated by Django 4.1.7 on 2023-04-25 21:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('why_inventory', '0005_alter_orderitem_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='unit_price',
        ),
    ]