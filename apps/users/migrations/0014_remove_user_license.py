# Generated by Django 4.2.11 on 2024-03-21 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_user_license'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='license',
        ),
    ]