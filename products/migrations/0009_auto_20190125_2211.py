# Generated by Django 2.1.5 on 2019-01-25 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_shoppingcart'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingcart',
            name='total_price',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='shoppingcart',
            name='user_address',
            field=models.CharField(default='unknown', max_length=200),
        ),
        migrations.AddField(
            model_name='shoppingcart',
            name='user_name',
            field=models.CharField(default='unknown', max_length=30),
        ),
    ]