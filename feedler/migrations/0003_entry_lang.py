# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 20:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedler', '0002_feedpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='lang',
            field=models.CharField(blank=True, default='', max_length=2),
        ),
    ]
