# Generated by Django 4.2 on 2023-05-07 23:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_alter_adddrug_date_of_entering_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adddrug',
            name='date_of_entering',
            field=models.DateField(default=datetime.datetime(2023, 5, 7, 18, 58, 0, 793788), verbose_name='تاريخ الإدخال'),
        ),
        migrations.AlterField(
            model_name='billsale',
            name='num_bill',
            field=models.CharField(default='7905', max_length=100, verbose_name='رقم الفاتورة'),
        ),
        migrations.DeleteModel(
            name='Product_bill',
        ),
    ]
