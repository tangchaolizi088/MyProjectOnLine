# Generated by Django 2.2.3 on 2019-07-10 05:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_banner_emailverifyrecord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 10, 13, 9, 20, 14233), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 10, 13, 9, 20, 14233)),
        ),
    ]
