# Generated by Django 4.2.11 on 2024-03-21 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_alter_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='license',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_related_license', to='users.license'),
        ),
    ]
