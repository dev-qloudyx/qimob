# Generated by Django 4.2.10 on 2024-02-27 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0008_clientmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='ident_doc',
            field=models.CharField(max_length=15, null=True, unique=True, verbose_name='identity doc'),
        ),
        migrations.AddField(
            model_name='client',
            name='nif',
            field=models.CharField(max_length=9, null=True, unique=True, verbose_name='NIF'),
        ),
        migrations.AddField(
            model_name='client',
            name='url',
            field=models.CharField(null=True, unique=True, verbose_name='social link'),
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]
