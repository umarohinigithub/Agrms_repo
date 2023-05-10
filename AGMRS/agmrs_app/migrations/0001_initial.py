# Generated by Django 4.2 on 2023-05-06 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgmDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('device_id', models.CharField(max_length=100, unique=True)),
                ('loacation', models.CharField(max_length=100)),
                ('present_value', models.FloatField(default=0)),
                ('average_value', models.FloatField(default=0)),
                ('date_time', models.DateTimeField(auto_now=True)),
                ('battery_percentage', models.FloatField()),
                ('status', models.CharField(choices=[('alarm', 'Alarm'), ('normal', 'Normal')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='AgrmsEmployee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('employee_id', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TelidosiDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('total_dose', models.IntegerField()),
                ('count', models.IntegerField()),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='agmrs_app.agrmsemployee')),
            ],
        ),
    ]
