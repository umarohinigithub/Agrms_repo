import django_tables2 as tables
from django.urls import reverse
from django.utils.html import format_html

from .models import AgrmsEmployee, AgmDevice, TelidosiDevice, AgmDeviceData


class EmployeeTable(tables.Table):
    edit = tables.Column(empty_values=(), verbose_name='Edit')
    delete = tables.Column(empty_values=(), verbose_name='Delete')

    class Meta:
        model = AgrmsEmployee
        template_name = "django_tables2/bootstrap.html"
        attrs = {'class': 'table table-sm'}
        fields = ('employee_id', 'name')  # Add more fields as needed

    def render_edit(self, value, record):
        edit_url = reverse('edit_employee_view', kwargs={'employee_id': record.id})
        return format_html(f'<a href="{edit_url}" class="btn btn-primary">Edit</a>')

    def render_delete(self, value, record):
        delete_url = reverse('delete_employee_view', kwargs={'employee_id': record.id})
        return format_html(f'<a href="{delete_url}" class="btn btn-primary">Delete</a>')

class AgmIndoorTable(tables.Table):
    edit = tables.Column(empty_values=(), verbose_name='Edit')
    delete = tables.Column(empty_values=(), verbose_name='Delete')

    class Meta:
        model = AgmDevice
        template_name = "django_tables2/bootstrap.html"
        attrs = {"class": "table table-container table-responsive table-hover"}
        fields = ['device_type', 'name', 'device_id' ]

    def render_edit(self, value, record):
        edit_url = reverse('edit_agm_indoor_view', kwargs={'device_id': record.id})
        return format_html(f'<a href="{edit_url}" class="btn btn-primary">Edit</a>')

    def render_delete(self, value, record):
        delete_url = reverse('delete_agm_indoor_view', kwargs={'device_id': record.id})
        return format_html(f'<a href="{delete_url}" class="btn btn-primary">Delete</a>')

class TeledosimeterTable(tables.Table):
    edit = tables.Column(empty_values=(), verbose_name='Edit')
    delete = tables.Column(empty_values=(), verbose_name='Delete')

    class Meta:
        model = TelidosiDevice
        template_name = "django_tables2/bootstrap.html"
        attrs = {'class': 'table table-sm'}
        # fields = ('employee_id', 'name')  # Add more fields as needed
        fields = ['name', 'device_id','employee_name']

    def render_edit(self, value, record):
        edit_url = reverse('edit_teledosimeter_view', kwargs={'device_id': record.id})
        return format_html(f'<a href="{edit_url}" class="btn btn-primary">Edit</a>')

    def render_delete(self, value, record):
        delete_url = reverse('delete_teledosimeter_view', kwargs={'device_id': record.id})
        return format_html(f'<a href="{delete_url}" class="btn btn-primary">Delete</a>')


class DevicedataViewMore(tables.Table):
    # edit = tables.Column(empty_values=(), verbose_name='Edit')
    battery = tables.Column(empty_values=(), verbose_name='Battery Percentage')

    class Meta:
        model = AgmDeviceData
        template_name = "django_tables2/bootstrap.html"
        attrs = {'class': 'table table-sm'}
        fields = ['device', 'location', 'present_value', 'average_value', 'date_time', 'status']

    def render_battery(self, value, record):
        battery_percentage = record.battery_percentage
        if battery_percentage >= 90:
            return format_html(f'{record.battery_percentage}<div class="progress progress-xs"><div class="progress-bar progress-bar-green" style="width: 90%" role="progressbar" aria-valuenow="20" aria-valuemin="0" aria-valuemax="100"><span class="sr-only">90% Complete</span></div></div>')
        if battery_percentage >= 75:
            return format_html(f'{record.battery_percentage}<div class="progress progress-xs"><div class="progress-bar progress-bar-green" style="width: 80%" role="progressbar" aria-valuenow="20" aria-valuemin="0" aria-valuemax="100"><span class="sr-only">80% Complete</span></div></div>')
        if battery_percentage >= 50:
            return format_html(f'{record.battery_percentage}<div class="progress progress-xs"><div class="progress-bar progress-bar-aqua" style="width: 50%" role="progressbar" aria-valuenow="20" aria-valuemin="0" aria-valuemax="100"><span class="sr-only">50% Complete</span></div></div>')
        if battery_percentage >= 25:
            return format_html(f'{record.battery_percentage}<div class="progress progress-xs"><div class="progress-bar progress-bar-yellow" style="width: 25%" role="progressbar" aria-valuenow="20" aria-valuemin="0" aria-valuemax="100"><span class="sr-only">25% Complete</span></div></div>')
        if battery_percentage <= 25:
            return format_html(f'{record.battery_percentage}<div class="progress progress-xs"><div class="progress-bar progress-bar-red" style="width: 10%" role="progressbar" aria-valuenow="20" aria-valuemin="0" aria-valuemax="100"><span class="sr-only">5% Complete</span></div></div>')
        if battery_percentage == 100:
            return format_html(f'{record.battery_percentage}<div class="progress progress-xs"><div class="progress-bar progress-bar-green" style="width: 100%" role="progressbar" aria-valuenow="20" aria-valuemin="0" aria-valuemax="100"><span class="sr-only">100% Complete</span></div></div>')
