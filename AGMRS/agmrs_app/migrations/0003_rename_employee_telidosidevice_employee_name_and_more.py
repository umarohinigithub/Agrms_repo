# Generated by Django 4.2 on 2023-05-08 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agmrs_app', '0002_rename_loacation_agmdevice_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='telidosidevice',
            old_name='employee',
            new_name='employee_name',
        ),
        migrations.AlterField(
            model_name='agmdevice',
            name='battery_percentage',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='agmdevice',
            name='present_value',
            field=models.FloatField(),
        ),
    ]
