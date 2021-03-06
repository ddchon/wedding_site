# Generated by Django 3.0 on 2019-12-17 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RSVP', '0007_remove_guest_plus_ones'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='plus_ones',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='guestparty',
            name='guest',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='RSVP.Guest'),
        ),
    ]
