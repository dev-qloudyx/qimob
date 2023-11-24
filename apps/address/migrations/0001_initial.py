# Generated by Django 4.2.7 on 2023-11-23 10:29

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('project', models.CharField(max_length=255, null=True)),
                ('app', models.CharField(max_length=255, null=True)),
                ('model', models.CharField(max_length=255, null=True)),
                ('cp4', models.IntegerField()),
                ('cp3', models.IntegerField()),
                ('postal_code', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('county', models.CharField(max_length=100)),
                ('locality', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=100)),
                ('more_info', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
            ],
        ),
        migrations.CreateModel(
            name='CountyData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CC', models.CharField(max_length=255)),
                ('DESIG', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DistrictData',
            fields=[
                ('DD', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('DESIG', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CPData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LLLL', models.CharField(max_length=255)),
                ('LOCALIDADE', models.CharField(max_length=255)),
                ('ART_COD', models.CharField(max_length=255)),
                ('ART_TIPO', models.CharField(max_length=255)),
                ('PRI_PREP', models.CharField(max_length=255)),
                ('ART_TITULO', models.CharField(max_length=255)),
                ('SEG_PREP', models.CharField(max_length=255)),
                ('ART_DESIG', models.CharField(max_length=255)),
                ('ART_LOCAL', models.CharField(max_length=255)),
                ('TROÇO', models.CharField(max_length=255)),
                ('PORTA', models.CharField(max_length=255)),
                ('CLIENTE', models.CharField(max_length=255)),
                ('CP4', models.CharField(max_length=255)),
                ('CP3', models.CharField(max_length=255)),
                ('CPALF', models.CharField(max_length=255)),
                ('CC', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='address.countydata')),
                ('DD', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='address.districtdata')),
            ],
        ),
        migrations.AddField(
            model_name='countydata',
            name='DD',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='address.districtdata'),
        ),
    ]
