# Generated by Django 4.2.11 on 2024-03-20 09:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0019_alter_clientaddress_client_leadshare'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prospects',
            name='partyphone',
            field=models.BigIntegerField(validators=[django.core.validators.MinValueValidator(200000000), django.core.validators.MaxValueValidator(999999999)]),
        ),
    ]
