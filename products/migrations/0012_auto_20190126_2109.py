# Generated by Django 2.1.5 on 2019-01-26 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20190126_2010'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shoppingcart',
            options={'ordering': ('order_completed', '-payment_completed')},
        ),
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.CharField(default='', max_length=200),
        ),
    ]
