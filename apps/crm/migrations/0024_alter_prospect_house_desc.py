# Generated by Django 4.2.11 on 2024-04-03 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0023_prospect_created_at_prospect_created_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prospect',
            name='house_desc',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='desc'),
        ),
    ]
