# Generated by Django 3.1.6 on 2021-02-19 15:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0004_auto_20210219_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='list_date',
            field=models.DateTimeField(blank=True, verbose_name=datetime.datetime(2021, 2, 19, 21, 28, 52, 828526)),
        ),
    ]