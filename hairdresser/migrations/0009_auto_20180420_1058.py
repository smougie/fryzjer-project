# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-20 08:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hairdresser', '0008_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products_photos'),
        ),
        migrations.AlterField(
            model_name='saloninfo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='salon_photo'),
        ),
    ]