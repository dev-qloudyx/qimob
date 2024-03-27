# Generated by Django 4.2.11 on 2024-03-27 12:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('imovel', '0005_remove_imovel_license'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imovel',
            name='address',
        ),
        migrations.AddField(
            model_name='imovel',
            name='availability',
            field=models.BooleanField(default=True, verbose_name='Availability'),
        ),
        migrations.AddField(
            model_name='imovel',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AddField(
            model_name='imovel',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='imovel',
            name='gps_latitude',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Latitude'),
        ),
        migrations.AddField(
            model_name='imovel',
            name='gps_longitude',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Longitude'),
        ),
        migrations.AddField(
            model_name='imovel',
            name='phone_number',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='phone number'),
        ),
        migrations.AddField(
            model_name='imovel',
            name='url',
            field=models.URLField(blank=True, null=True, verbose_name='URL'),
        ),
        migrations.AddField(
            model_name='imovel',
            name='url_map',
            field=models.URLField(blank=True, null=True, verbose_name='URL Map'),
        ),
        migrations.AddField(
            model_name='imovel',
            name='visit_timeslots',
            field=models.CharField(blank=True, null=True, verbose_name='Visits Time Slots'),
        ),
        migrations.AlterField(
            model_name='imovel',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.CreateModel(
            name='ImovelAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=255, verbose_name='token')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('deleted', models.BooleanField(default=False)),
                ('imovel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imovel_address', to='imovel.imovel')),
            ],
        ),
    ]