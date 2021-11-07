# Generated by Django 3.2.5 on 2021-11-07 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0002_remove_booking_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='parking_id',
            field=models.IntegerField(default=0, max_length=2),
        ),
        migrations.AddField(
            model_name='booking',
            name='vehicle_no',
            field=models.IntegerField(default=8989, max_length=100),
        ),
    ]
