# Generated by Django 3.2.5 on 2021-07-20 12:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='date_enrolled',
            field=models.DateField(default=datetime.datetime(2021, 7, 20, 12, 34, 33, 596193)),
        ),
    ]
