# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-02 00:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
