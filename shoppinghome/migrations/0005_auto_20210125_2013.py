# Generated by Django 3.1.5 on 2021-01-25 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppinghome', '0004_auto_20210125_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_img',
            field=models.CharField(max_length=200),
        ),
    ]
