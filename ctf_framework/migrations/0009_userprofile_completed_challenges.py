# Generated by Django 2.0.1 on 2018-05-23 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ctf_framework', '0008_auto_20180523_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='completed_challenges',
            field=models.ManyToManyField(through='ctf_framework.ChallengeSolve', to='ctf_framework.Challenge'),
        ),
    ]
