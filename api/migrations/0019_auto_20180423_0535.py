# Generated by Django 2.0.3 on 2018-04-23 04:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_notification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilepicture',
            name='account',
        ),
        migrations.DeleteModel(
            name='ProfilePicture',
        ),
    ]