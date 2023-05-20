# Generated by Django 4.0.4 on 2023-05-19 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0002_alter_stream_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cdz',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name': 'cdz',
                'verbose_name_plural': 'cdzs',
                'db_table': 'cdz',
            },
        ),
    ]