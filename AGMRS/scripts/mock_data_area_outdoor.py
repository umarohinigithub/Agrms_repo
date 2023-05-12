"""
Usage: python manage.py runscript mock_data_area_outdoor
"""


from agmrs_app.models import AgmDevice, AgmDeviceData
import random
import time


def run():
    agrms_outdoor_devices = AgmDevice.objects.all()
    while True:
        print("Running mock_data_area_outdoor", time.time())
        for device in agrms_outdoor_devices:
            random_battery = random.randint(20, 100)
            random_present = random.randint(5, 20)
            AgmDeviceData.objects.create(device=device, location='Plamoodu', battery_percentage=random_battery,
                                         present_value=random_present,
                                         average_value=10, status=AgmDeviceData.ALARM)

        time.sleep(10)