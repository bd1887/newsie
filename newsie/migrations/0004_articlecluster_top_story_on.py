# Generated by Django 2.1.7 on 2019-04-18 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsie', '0003_auto_20190416_2128'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlecluster',
            name='top_story_on',
            field=models.DateTimeField(null=True),
        ),
    ]
