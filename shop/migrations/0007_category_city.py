# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-28 09:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20170328_0834'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='city',
            field=models.ForeignKey(default=231, on_delete=django.db.models.deletion.CASCADE, to='shop.City', verbose_name='Город'),
            preserve_default=False,
        ),
    ]
