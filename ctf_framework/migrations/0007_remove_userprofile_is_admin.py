# Generated by Django 2.0.1 on 2018-05-21 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ctf_framework', '0006_auto_20180207_2113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='is_admin',
        ),
    ]