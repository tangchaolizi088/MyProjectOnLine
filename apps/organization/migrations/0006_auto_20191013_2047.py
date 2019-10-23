# Generated by Django 2.2.3 on 2019-10-13 12:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0005_auto_20191010_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='course_nums',
            field=models.IntegerField(default=0, verbose_name='课程数'),
        ),
        migrations.AddField(
            model_name='courseorg',
            name='students',
            field=models.IntegerField(default=0, verbose_name='学习人数'),
        ),
        migrations.AlterField(
            model_name='citydict',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 13, 20, 47, 25, 775148)),
        ),
        migrations.AlterField(
            model_name='courseorg',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 13, 20, 47, 25, 776149)),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 13, 20, 47, 25, 776149)),
        ),
    ]
