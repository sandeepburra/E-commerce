# Generated by Django 3.1.5 on 2021-01-24 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asin', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asin', models.CharField(max_length=50)),
                ('product_type_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Type2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asin', models.CharField(max_length=50)),
                ('product_type_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Type3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asin', models.CharField(max_length=50)),
                ('product_type_name', models.CharField(max_length=50)),
            ],
        ),
    ]
