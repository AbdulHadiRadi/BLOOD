# Generated by Django 2.0.2 on 2018-03-31 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20180331_0203'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='street',
            new_name='street_number',
        ),
    ]
