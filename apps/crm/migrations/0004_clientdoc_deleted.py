# Generated by Django 4.2.7 on 2023-11-12 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_clientdoc_created_at_clientdoc_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientdoc',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]