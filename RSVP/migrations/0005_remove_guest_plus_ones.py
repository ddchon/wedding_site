# Generated by Django 3.0 on 2019-12-16 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RSVP', '0004_guest_plus_ones'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guest',
            name='plus_ones',
        ),
    ]