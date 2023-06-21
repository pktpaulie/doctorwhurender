# Generated by Django 4.1.7 on 2023-05-01 09:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('why_inventory', '0007_customar_ordar_ordaritem'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(to='why_inventory.inventory'),
        ),
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.PositiveIntegerField(default=1, null=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=200, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]