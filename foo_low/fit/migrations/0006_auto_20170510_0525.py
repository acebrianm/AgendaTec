# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-10 05:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fit', '0005_auto_20170509_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(upload_to='fit/static/fit/images'),
        ),
    ]