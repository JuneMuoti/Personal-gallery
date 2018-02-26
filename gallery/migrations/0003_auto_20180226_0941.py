# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-26 06:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20180223_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='url',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='image',
            name='gallery_image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
