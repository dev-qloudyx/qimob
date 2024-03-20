# Generated by Django 4.2.11 on 2024-03-19 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_rename_config_id_license_config_and_more'),
        ('crm', '0016_alter_client_license_alter_lead_license'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leadstatus',
            name='lead_desc',
        ),
        migrations.RemoveField(
            model_name='leadstatus',
            name='updated_on',
        ),
        migrations.AddField(
            model_name='leadstatus',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='status_code', to='users.statuscode', verbose_name='status'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='client',
            name='license',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_license', to='users.license'),
        ),
        migrations.AlterField(
            model_name='lead',
            name='license',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lead_license', to='users.license'),
        ),
        migrations.DeleteModel(
            name='LeadStatusDesc',
        ),
        migrations.DeleteModel(
            name='License',
        ),
    ]