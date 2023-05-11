"""
Usage: python manage.py runscript mock_data_teledosi
"""


from agmrs_app.models import TelidosiDevice, TelidosiData
import random
import time


def run():
    agrms_teledosi_devices = TelidosiDevice.objects.all()

    while True:
        print("Running mock_data_teledosi", time.time())
        for device in agrms_teledosi_devices:
            random_total_dose = random.randint(20, 100)
            random_count = random.randint(5, 20)
            TelidosiData.objects.create(device=device, total_dose=random_total_dose,
                                         count=random_count,
                                         )

        time.sleep(10)