# Generated by Django 4.2 on 2023-05-07 18:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_adddrug_options_remove_adddrug_cost_of_big_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adddrug',
            name='date_of_entering',
            field=models.DateField(default=datetime.datetime(2023, 5, 7, 13, 21, 13, 650754), verbose_name='تاريخ الإدخال'),
        ),
        migrations.AlterField(
            model_name='billsale',
            name='num_bill',
            field=models.CharField(default='1492', max_length=100, verbose_name='رقم الفاتورة'),
        ),
        migrations.AlterField(
            model_name='product_bill',
            name='num_bill',
            field=models.CharField(default='1492', max_length=100, verbose_name='رقم الفاتورة'),
        ),
    ]