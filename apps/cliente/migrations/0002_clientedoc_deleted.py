# Generated by Django 4.2.7 on 2023-11-09 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientedoc',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
