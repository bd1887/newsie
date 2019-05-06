# Generated by Django 2.1.7 on 2019-05-06 11:09

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsie', '0007_auto_20190506_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='authors',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=1000), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='article',
            name='manual_label',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='article',
            name='tokens',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=1000), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='article',
            name='url',
            field=models.URLField(max_length=1000, unique=True),
        ),
        migrations.AlterField(
            model_name='articlecluster',
            name='category',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
