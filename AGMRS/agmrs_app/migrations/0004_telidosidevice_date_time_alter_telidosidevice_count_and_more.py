# Generated by Django 4.2 on 2023-05-09 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agmrs_app', '0003_rename_employee_telidosidevice_employee_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='telidosidevice',
            name='date_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='telidosidevice',
            name='count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='telidosidevice',
            name='total_dose',
            field=models.IntegerField(default=0),
        ),
    ]
