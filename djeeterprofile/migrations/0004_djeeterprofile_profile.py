# Generated by Django 2.0.5 on 2018-06-30 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djeeterprofile', '0003_djeeterprofile_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='djeeterprofile',
            name='profile',
            field=models.CharField(default='', max_length=140),
        ),
    ]
