from django.db import models


# Create your models here.
class AgrmsEmployee(models.Model):
    name = models.CharField(max_length=200)
    employee_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class TelidosiDevice(models.Model):
    device_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    employee_name = models.ForeignKey(AgrmsEmployee, on_delete=models.SET_NULL, null=True)
    total_dose = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    date_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name


class AgmDevice(models.Model):
    DEVICE_TYPE_CHOICES = [
        ('indoor', 'Indoor'),
        ('outdoor', 'Outdoor'),
    ]
    STATUS_CHOICES = (
        ('alarm', 'Alarm'),
        ('normal', 'Normal'),
    )
    name = models.CharField(max_length=100)
    device_id = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=100)
    present_value = models.FloatField()
    average_value = models.FloatField(default=0)
    date_time = models.DateTimeField(auto_now=True)
    battery_percentage = models.FloatField(default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    device_type = models.CharField(max_length=10,choices=DEVICE_TYPE_CHOICES)
    def __str__(self):
        return self.name
