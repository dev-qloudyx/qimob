# Generated by Django 4.2.11 on 2024-03-19 18:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crm', '0018_alter_leadstatus_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientaddress',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_address', to='crm.client'),
        ),
        migrations.CreateModel(
            name='LeadShare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('can_read', models.BooleanField(default=True, verbose_name='can read')),
                ('can_write', models.BooleanField(default=False, verbose_name='can write')),
                ('lead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.lead')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]