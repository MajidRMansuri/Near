# Generated by Django 4.0.4 on 2022-04-26 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nearin_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Shop_register',
            new_name='Shop_login',
        ),
        migrations.AlterModelTable(
            name='shop_login',
            table='shop_login',
        ),
    ]