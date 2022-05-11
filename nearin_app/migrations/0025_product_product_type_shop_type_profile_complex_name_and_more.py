# Generated by Django 4.0.4 on 2022-05-10 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nearin_app', '0024_state_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Image', models.FileField(default='images/product.png', upload_to='images/users')),
                ('Prod_name', models.CharField(default='', max_length=25)),
                ('Prod_type', models.CharField(default='', max_length=25)),
                ('Prod_price', models.FloatField(default='', max_length=25)),
                ('Prod_des', models.TextField(default='', max_length=255)),
                ('Availability', models.CharField(choices=[('y', 'yes'), ('n', 'no')], max_length=10)),
            ],
            options={
                'db_table': 'Product',
            },
        ),
        migrations.CreateModel(
            name='Product_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_type', models.CharField(default='', max_length=25)),
            ],
            options={
                'db_table': 'Product_type',
            },
        ),
        migrations.CreateModel(
            name='Shop_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Shop_type', models.CharField(default='', max_length=25)),
            ],
            options={
                'db_table': 'Shop_type',
            },
        ),
        migrations.AddField(
            model_name='profile',
            name='Complex_name',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AddField(
            model_name='profile',
            name='House_no',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AddField(
            model_name='shop_profile',
            name='Shop_complex',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AddField(
            model_name='shop_profile',
            name='Shop_no',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AddField(
            model_name='shop_profile',
            name='Shop_type',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AddField(
            model_name='shop_profile',
            name='owner_name',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AlterField(
            model_name='profile',
            name='Contact',
            field=models.CharField(default='', max_length=12),
        ),
        migrations.AlterField(
            model_name='shop_profile',
            name='Contact',
            field=models.CharField(default='', max_length=12),
        ),
    ]
