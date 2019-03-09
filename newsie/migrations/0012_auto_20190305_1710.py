# Generated by Django 2.1.5 on 2019-03-05 17:10

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsie', '0011_article_tokens'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tokens',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=500), blank=True, default=list, size=None),
        ),
    ]
