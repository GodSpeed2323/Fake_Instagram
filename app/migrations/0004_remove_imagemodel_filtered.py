# Generated by Django 2.0 on 2018-01-03 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20171228_1940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagemodel',
            name='filtered',
        ),
    ]