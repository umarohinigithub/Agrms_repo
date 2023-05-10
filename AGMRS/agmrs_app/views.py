from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import TemplateView, FormView, ListView, UpdateView, DeleteView
from django_filters.views import FilterView
from django_tables2 import SingleTableView

from agmrs_app.filter import EmployeeFilter
from agmrs_app.forms import AdminLoginForm, AddEmployeeForm, EditEmployeeForm, AddAgmIndoorForm, EditAgmIndoorForm, \
    AddTeledosimeterForm, EditTeledosimeterForm
from agmrs_app.models import AgrmsEmployee, AgmDevice, TelidosiDevice
from agmrs_app.table import EmployeeTable, AgmIndoorTable, TeledosimeterTable


# Create your views here.
# class AdminDashboardView(TemplateView):
#     template_name = 'agmrs_app/login.html'

class AdminLoginView(FormView):
    template_name = 'agmrs_app/login.html'
    form_class = AdminLoginForm

    def get_success_url(self):
        return reverse('admin_login_view')

    def post(self, request, *args, **kwargs):
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            print("user available ")
            return redirect('dashboard_view')
        else:
            print("user not available")
        return super().post(request, *args, **kwargs)


class AdminLogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('admin_login_view')


class AdminDashBoardView(TemplateView):
    template_name = 'agmrs_app/dashboard.html'


class TestTemplateView(TemplateView):
    template_name = 'agmrs_app/area_gamma_monitor.html'


class AgmIndoorView(TemplateView):
    template_name = 'agmrs_app/agm_indoor.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = AgmDevice.objects.filter(device_type='indoor').order_by('-date_time')[:7]
        return context


# class AgmOutdoorView(TemplateView):
#     template_name = 'agmrs_app/agm_outdoor.html'


class AgmOutdoorView(TemplateView):
    template_name = 'agmrs_app/agm_outdoor.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['datas'] = AgmDevice.objects.filter(device_type='outdoor').order_by('-date_time')[:8]
        return context


class TeledosiView(TemplateView):
    template_name = 'agmrs_app/teledosimeter.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teledata'] = TelidosiDevice.objects.order_by('-date_time')[:5]
        return context


class AddEmployeeView(FormView):
    template_name = 'agmrs_app/agm_employee/add_employee.html'
    form_class = AddEmployeeForm
    model = AgrmsEmployee
    success_url = reverse_lazy('list_employee_view')

    # success_url = reverse_lazy('dashboard_view')

    # def get_success_url(self):
    #     return reverse('dashboard_view')

    def form_valid(self, form):
        if form.is_valid():
            data = form.cleaned_data
            # employee_id = form.cleaned_data['employee_id']
            # name = form.cleaned_data['name']
            # print(name)
            form.save()
            return redirect('list_employee_view')
        else:
            print(form.errors)


class ListEmployeeView(SingleTableView, FilterView):
    model = AgrmsEmployee
    table_class = EmployeeTable
    template_name = 'agmrs_app/agm_employee/list_employee.html'
    context_table_name = 'table'
    paginate_by = 3
    # filterset_class = EmployeeFilter


class EditEmployeeView(UpdateView):
    model = AgrmsEmployee
    # fields = '__all()__'
    form_class = EditEmployeeForm
    template_name = 'agmrs_app/agm_employee/edit_employee.html'
    pk_url_kwarg = 'employee_id'
    success_url = reverse_lazy('list_employee_view')

    def get_object(self, queryset=None):
        employee_id = self.kwargs.get('employee_id')
        return self.model.objects.get(id=employee_id)


class DeleteEmployeeView(DeleteView):
    model = AgrmsEmployee
    fields = '__all()__'
    template_name = 'agmrs_app/agm_employee/delete_employee.html'
    pk_url_kwarg = 'employee_id'
    success_url = reverse_lazy('list_employee_view')
    ordering = 'employee_id'  # Specify the ordering field here


class AddAgmIndoorView(FormView):
    template_name = 'agmrs_app/agm_indoor/add_agm_indoor.html'
    form_class = AddAgmIndoorForm
    model = AgmDevice
    success_url = reverse_lazy('dashboard_view')

    # success_url = reverse_lazy('dashboard_view')

    def form_valid(self, form):

        form.instance = AgmDevice()
        form.instance.name = form.cleaned_data['name']
        form.instance.device_id = form.cleaned_data['device_id']
        form.instance.location = form.cleaned_data['location']
        form.instance.present_value = form.cleaned_data['present_value']
        form.instance.average_value = form.cleaned_data['average_value']
        form.instance.battery_percentage = form.cleaned_data['battery_percentage']
        form.instance.device_type = form.cleaned_data['device_type']

        # Set the status based on the condition
        if form.instance.present_value > (0.5 * form.instance.average_value):
            form.instance.status = 'ALARM'
        else:
            form.instance.status = 'NORMAL'

        # Save the form instance
        form.instance.save()

        return redirect(self.success_url)


class ListAgmIndoorView(SingleTableView, FilterView):
    model = AgmDevice
    table_class = AgmIndoorTable
    template_name = 'agmrs_app/agm_indoor/list_agm_indoor.html'
    context_table_name = 'table'
    paginate_by = 3
    ordering = ['id']
    # filterset_class = EmployeeFilter


class EditAgmIndoorView(UpdateView):
    model = AgmDevice
    # fields = '__all()__'
    form_class = EditAgmIndoorForm
    template_name = 'agmrs_app/agm_indoor/edit_agm_indoor.html'
    pk_url_kwarg = 'device_id'
    success_url = reverse_lazy('list_agm_indoor_view')

    def get_object(self, queryset=None):
        device_id = self.kwargs.get('device_id')
        return self.model.objects.get(id=device_id)


class DeleteAgmIndoorView(DeleteView):
    model = AgmDevice
    fields = '__all__'
    template_name = 'agmrs_app/agm_indoor/delete_agm_indoor.html'
    pk_url_kwarg = 'device_id'
    success_url = reverse_lazy('list_agm_indoor_view')


class AddTeledosimeterView(FormView):
    template_name = 'agmrs_app/teledosimeter/add_teledosimeter.html'
    form_class = AddTeledosimeterForm
    model = AgmDevice
    success_url = reverse_lazy('list_teledosimeter_view')

    # success_url = reverse_lazy('dashboard_view')

    def form_valid(self, form):
        form.instance = TelidosiDevice()
        form.instance.name = form.cleaned_data['name']
        form.instance.device_id = form.cleaned_data['device_id']
        form.instance.location = form.cleaned_data['total_dose']
        form.instance.present_value = form.cleaned_data['count']
        # Save the form instance
        employee_name = form.cleaned_data['employee_name']
        employee = AgrmsEmployee.objects.get(name=employee_name)

        # Assign the employee instance to the employee_name field
        form.instance.employee_name = employee
        form.instance.save()

        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employees'] = AgrmsEmployee.objects.all()
        return context


class ListTeledosimeterView(SingleTableView, FilterView):
    model = TelidosiDevice
    table_class = TeledosimeterTable
    template_name = 'agmrs_app/teledosimeter/list_teledosimeter.html'
    context_table_name = 'table'
    paginate_by = 3
    ordering = ['id']
    # filterset_class = EmployeeFilter


class EditTeledosimeterView(UpdateView):
    model = TelidosiDevice
    # fields = '__all()__'
    form_class = EditTeledosimeterForm
    template_name = 'agmrs_app/teledosimeter/edit_teledosimeter.html'
    pk_url_kwarg = 'device_id'
    success_url = reverse_lazy('list_teledosimeter_view')

    def get_object(self, queryset=None):
        device_id = self.kwargs.get('device_id')
        return self.model.objects.get(id=device_id)


class DeleteTeledosimeterView(DeleteView):
    template_name = 'agmrs_app/teledosimeter/delete_teledosimeter.html'
    model = TelidosiDevice
    fields = '__all__'
    pk_url_kwarg = 'device_id'
    success_url = reverse_lazy('list_teledosimeter_view')
