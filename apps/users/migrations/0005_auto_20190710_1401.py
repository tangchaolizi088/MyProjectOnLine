# Generated by Django 2.2.3 on 2019-07-10 06:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190710_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 10, 14, 1, 59, 132924), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 10, 14, 1, 59, 132924)),
        ),
    ]
