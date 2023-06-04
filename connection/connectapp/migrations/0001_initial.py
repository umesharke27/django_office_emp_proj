# Generated by Django 4.1.7 on 2023-03-18 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product_details_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('prd_qnty', models.IntegerField()),
                ('prd_price', models.FloatField()),
                ('prd_loc', models.CharField(max_length=20)),
            ],
        ),
    ]
