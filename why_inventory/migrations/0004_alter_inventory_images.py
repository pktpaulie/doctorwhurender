# Generated by Django 4.1.7 on 2023-04-25 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('why_inventory', '0003_sale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
