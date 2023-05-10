
import django_filters
from .models import  AgrmsEmployee
from django.urls import reverse


class EmployeeFilter(django_filters.FilterSet):
    employee_name= django_filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = AgrmsEmployee
        fields = ['name']


