# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-12 12:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedler', '0005_auto_20170920_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='entry_id',
            field=models.CharField(blank=True, editable=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='feedlysettings',
            name='feedly_pages',
            field=models.IntegerField(blank=True, choices=[(1, '2'), (2, '5'), (3, '10'), (4, '50')], editable=False, help_text='How many pages to fetch?', null=True),
        ),
        migrations.AlterField(
            model_name='feedlysettings',
            name='feedly_stream',
            field=models.ManyToManyField(help_text='Which streams to update', to='feedler.Stream'),
        ),
    ]