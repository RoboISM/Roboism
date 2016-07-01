# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-16 14:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0002_auto_20160615_2233'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(null=True, upload_to=b'')),
                ('name', models.CharField(default=b'Name', max_length=50)),
                ('description', models.TextField(default=b'Shitty Project')),
                ('github', models.URLField(null=True)),
                ('completed', models.BooleanField()),
            ],
        ),
        migrations.AlterField(
            model_name='member',
            name='DOB',
            field=models.DateField(default=datetime.datetime(2016, 6, 16, 14, 14, 34, 584527, tzinfo=utc)),
        ),
    ]
