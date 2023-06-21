# Generated by Django 4.1.7 on 2023-04-24 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('why_inventory', '0002_alter_inventory_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sold_quantity', models.IntegerField(blank=True, default=0)),
                ('unit_price', models.IntegerField(blank=True, default=0)),
                ('paid_amount', models.IntegerField(blank=True, default=0)),
                ('customer_name', models.CharField(blank=True, max_length=50, null=True)),
                ('sold_date', models.DateTimeField(auto_now_add=True)),
                ('sold_item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='why_inventory.inventory')),
            ],
        ),
    ]