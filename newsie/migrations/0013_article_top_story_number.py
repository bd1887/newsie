# Generated by Django 2.1.5 on 2019-03-06 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsie', '0012_auto_20190305_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='top_story_number',
            field=models.IntegerField(max_length=1000, null=True),
        ),
    ]