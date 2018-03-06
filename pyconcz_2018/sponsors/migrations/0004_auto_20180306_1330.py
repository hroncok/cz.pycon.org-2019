# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-06 12:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0003_auto_20180306_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='facebook',
            field=models.URLField(blank=True, help_text='full URL', null=True),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='twitter',
            field=models.URLField(blank=True, help_text='full URL', null=True),
        ),
    ]