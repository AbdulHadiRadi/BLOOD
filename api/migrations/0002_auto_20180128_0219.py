# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-28 02:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_donor_or_hospital',
            new_name='is_donor',
        ),
    ]
