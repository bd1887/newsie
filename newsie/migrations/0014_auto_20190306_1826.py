# Generated by Django 2.1.5 on 2019-03-06 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsie', '0013_article_top_story_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='top_story_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]