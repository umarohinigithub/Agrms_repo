from django.contrib import admin

from agmrs_app.models import AgrmsEmployee ,TelidosiDevice, AgmDevice

# Register your models here.
admin.site.register(AgrmsEmployee)
admin.site.register(TelidosiDevice)
admin.site.register(AgmDevice)
