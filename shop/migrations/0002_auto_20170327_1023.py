# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-27 10:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['name'], 'verbose_name': 'Город', 'verbose_name_plural': 'Городв'},
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=150, unique=True, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='city',
            name='slug',
            field=models.SlugField(null=True, verbose_name='Транслит'),
        ),
        migrations.AlterModelTable(
            name='city',
            table='cyti',
        ),
    ]
