# Generated by Django 4.2.10 on 2024-02-27 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0009_client_ident_doc_client_nif_client_url_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='ident_doc',
        ),
        migrations.RemoveField(
            model_name='client',
            name='nif',
        ),
        migrations.RemoveField(
            model_name='client',
            name='url',
        ),
    ]
