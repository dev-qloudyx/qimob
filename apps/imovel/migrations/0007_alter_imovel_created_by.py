# Generated by Django 4.2.11 on 2024-03-27 12:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('imovel', '0006_remove_imovel_address_imovel_availability_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imovel',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
    ]
