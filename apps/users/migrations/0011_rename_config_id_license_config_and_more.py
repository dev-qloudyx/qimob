# Generated by Django 4.2.11 on 2024-03-18 12:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20240315_1233'),
    ]

    operations = [
        migrations.RenameField(
            model_name='license',
            old_name='config_ID',
            new_name='config',
        ),
        migrations.RenameField(
            model_name='statusconfig',
            old_name='config_ID',
            new_name='config',
        ),
        migrations.RenameField(
            model_name='workflowconfig',
            old_name='config_ID',
            new_name='config',
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_leader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.teamleader')),
                ('team_member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
