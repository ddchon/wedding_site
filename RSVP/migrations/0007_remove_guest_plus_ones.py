# Generated by Django 3.0 on 2019-12-17 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RSVP', '0006_guest_plus_ones'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guest',
            name='plus_ones',
        ),
    ]
