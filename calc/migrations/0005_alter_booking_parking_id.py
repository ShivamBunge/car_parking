# Generated by Django 3.2.5 on 2021-11-07 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0004_alter_booking_vehicle_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='parking_id',
            field=models.IntegerField(max_length=2),
        ),
    ]
