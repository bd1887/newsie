# Generated by Django 2.1.5 on 2019-03-09 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsie', '0017_article_labeled'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='labeled',
        ),
    ]
