import django_tables2 as tables
from django.urls import reverse
from django.utils.html import format_html

from .models import AgrmsEmployee, AgmDevice, TelidosiDevice


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
        attrs = {'class': 'table table-sm'}
        # fields = ('employee_id', 'name')  # Add more fields as needed
        fields = ['device_type','name', 'device_id' ]

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
