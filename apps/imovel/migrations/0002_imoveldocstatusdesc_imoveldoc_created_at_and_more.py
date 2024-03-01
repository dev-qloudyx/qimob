# Generated by Django 4.2.10 on 2024-02-29 11:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('imovel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImovelDocStatusDesc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=255, verbose_name='desc')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='updated on')),
            ],
        ),
        migrations.AddField(
            model_name='imoveldoc',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created at'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='imoveldoc',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='imoveldoc',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='updated at'),
        ),
        migrations.CreateModel(
            name='ImovelDocStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='updated on')),
                ('doc_desc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imoveldocstatus_imoveldocstatusdesc', to='imovel.imoveldocstatusdesc', verbose_name='doc desc')),
                ('imovel_doc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imoveldoc_status', to='imovel.imoveldoc', verbose_name='imoveldoc')),
            ],
        ),
    ]
