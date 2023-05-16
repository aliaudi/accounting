# Generated by Django 4.2 on 2023-05-10 05:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_product_bills_delete_product_bill_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adddrug',
            name='date_of_entering',
            field=models.DateField(default=datetime.datetime(2023, 5, 10, 0, 47, 47, 103181), verbose_name='تاريخ الإدخال'),
        ),
        migrations.AlterField(
            model_name='billsale',
            name='date',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='التاريخ'),
        ),
        migrations.AlterField(
            model_name='billsale',
            name='num_bill',
            field=models.CharField(default='6884', max_length=100, verbose_name='رقم الفاتورة'),
        ),
        migrations.AlterField(
            model_name='product_bills',
            name='date',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='التاريخ'),
        ),
        migrations.AlterField(
            model_name='product_bills',
            name='num_bill',
            field=models.CharField(default='6884', max_length=100, verbose_name='رقم الفاتورة'),
        ),
    ]