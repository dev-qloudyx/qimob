# Generated by Django 4.2.10 on 2024-02-29 11:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_profile_about_alter_profile_full_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_active',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Data Última Activação'),
        ),
        migrations.AddField(
            model_name='user',
            name='last_inactive',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Data Última Inactivação'),
        ),
        migrations.AddField(
            model_name='user',
            name='team_leader',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
