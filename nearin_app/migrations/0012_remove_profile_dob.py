# Generated by Django 4.0.4 on 2022-04-30 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nearin_app', '0011_remove_profile_profileimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='DOB',
        ),
    ]
