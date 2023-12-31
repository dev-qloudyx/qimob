# Generated by Django 4.2.7 on 2023-11-24 17:00

from django.db import migrations

def create_status_desc(apps, schema_editor):
    ClientDocStatusDesc = apps.get_model('crm', 'ClientDocStatusDesc')
    ClientDocStatusDesc.objects.create(desc='New')

class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0005_clientdocstatusdesc_rename_leads_consultantlead_lead_and_more'),
    ]

    operations = [
        migrations.RunPython(create_status_desc),
    ]

