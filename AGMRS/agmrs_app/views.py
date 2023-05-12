from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import TemplateView, FormView, ListView, UpdateView, DeleteView, CreateView
from django_filters.views import FilterView
from django_tables2 import SingleTableView

from agmrs_app.filter import EmployeeFilter
from agmrs_app.forms import AdminLoginForm, AddEmployeeForm, EditEmployeeForm, AddAgmIndoorForm, EditAgmIndoorForm, \
    AddTeledosimeterForm, EditTeledosimeterForm
from agmrs_app.models import AgrmsEmployee, AgmDevice, TelidosiDevice, AgmDeviceData, TelidosiData
from agmrs_app.table import EmployeeTable, AgmIndoorTable, TeledosimeterTable, DevicedataViewMore, TeledosidataViewMore


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

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['active_admin_dash'] = 'active treeview menu-open'
        context['indoor_count'] = AgmDevice.objects.filter(device_type=AgmDevice.INDOOR).count()
        context['outdoor_count'] = AgmDevice.objects.filter(device_type=AgmDevice.OUTDOOR).count()
        return context


class TestTemplateView(TemplateView):
    template_name = 'agmrs_app/area_gamma_monitor.html'


class AgmIndoorView(TemplateView):
    template_name = 'agmrs_app/agm_indoor.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        devices_indoor = AgmDevice.objects.filter(device_type=AgmDevice.INDOOR)
        data_ids = []
        for device in devices_indoor:
            device_data = AgmDeviceData.objects.filter(device=device).last()
            if device_data:
                data_ids.append(device_data.id)
        context['device_data'] = AgmDeviceData.objects.filter(id__in=data_ids)
        context['active_admin_dash'] = 'active treeview menu-open'
        return context


# class AgmOutdoorView(TemplateView):
#     template_name = 'agmrs_app/agm_outdoor.html'

def get_current_data_outdoor(request):
    print("get_current_data_outdoor")
    context = {}
    if request.htmx:
        devices_outdoor = AgmDevice.objects.filter(device_type=AgmDevice.OUTDOOR)
        data_ids = []
        for device in devices_outdoor:
            device_data = AgmDeviceData.objects.filter(device=device).last()
            if device_data:
                data_ids.append(device_data.id)
        print("+++++++++++++++++", data_ids)
        context['device_data'] = AgmDeviceData.objects.filter(id__in=data_ids)
        return render(request, template_name='agmrs_app/agm_outdoor_partial.html', context=context)


def get_current_data_indoor(request):
    print("get_current_data_indoor")
    context = {}
    if request.htmx:
        devices_indoor = AgmDevice.objects.filter(device_type=AgmDevice.INDOOR)
        data_ids = []
        for device in devices_indoor:
            device_data = AgmDeviceData.objects.filter(device=device).last()
            if device_data:
                data_ids.append(device_data.id)
        print("+++++++++++++++++", data_ids)
        context['device_data'] = AgmDeviceData.objects.filter(id__in=data_ids)
        return render(request, template_name='agmrs_app/agm_indoor_partial.html', context=context)

def get_current_data_teledosi(request):
    print("get_current_data_teledosi")
    context = {}
    if request.htmx:
        devices_teledosi = TelidosiDevice.objects.all()
        data_ids = []
        for device in devices_teledosi:
            device_data = TelidosiData.objects.filter(device=device).last()
            if device_data:
                data_ids.append(device_data.id)
        # print("+++++++++++++++++", data_ids)
        context['device_data'] = TelidosiData.objects.filter(id__in=data_ids)
        return render(request, template_name='agmrs_app/teledosimeter_partial.html', context=context)


class AgmOutdoorView(TemplateView):
    template_name = 'agmrs_app/agm_outdoor.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        devices_outdoor = AgmDevice.objects.filter(device_type=AgmDevice.OUTDOOR)
        data_ids = []
        for device in devices_outdoor:
            device_data = AgmDeviceData.objects.filter(device=device).last()
            if device_data:
                data_ids.append(device_data.id)
        print("+++++++++++++++++", data_ids)
        context['device_data'] = AgmDeviceData.objects.filter(id__in=data_ids)
        context['active_admin_dash'] = 'active treeview menu-open'
        return context


class TeledosiView(TemplateView):
    template_name = 'agmrs_app/teledosimeter.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        devices_teledosi = TelidosiDevice.objects.all()
        data_ids = []
        for device in devices_teledosi:
            device_data = TelidosiData.objects.filter(device=device).last()
            if device_data:
                data_ids.append(device_data.id)
        # print("+++++++++++++++++", data_ids)
        context['device_data'] = TelidosiData.objects.filter(id__in=data_ids)
        context['active_admin_dash'] = 'active treeview menu-open'
        return context


class AddEmployeeView(FormView):
    template_name = 'agmrs_app/agm_employee/add_employee.html'
    form_class = AddEmployeeForm
    model = AgrmsEmployee
    success_url = reverse_lazy('list_employee_view')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['active_teledosimeter'] = 'active treeview menu-open'
        context['active_teledosimeter_add_emp'] = 'active'
        return context

    # def form_valid(self, form):
    #     if form.is_valid():
    #         data = form.cleaned_data
    #         # employee_id = form.cleaned_data['employee_id']
    #         # name = form.cleaned_data['name']
    #         # print(name)
    #         form.save()
    #         return redirect('list_employee_view')
    #     else:
    #         print(form.errors)


class ListEmployeeView(SingleTableView, FilterView):
    model = AgrmsEmployee
    table_class = EmployeeTable
    template_name = 'agmrs_app/agm_employee/list_employee.html'
    context_table_name = 'table'
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['active_teledosimeter'] = 'treeview active'
        context['active_teledosimeter_list_emp'] = 'active'
        return context


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

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeleteEmployeeView, self).delete(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_imp_operator'] = "active"  # sidebar active tag
        context['active_imp_users'] = "active openable open"  # sidebar active tag
        return context


class AddAgmIndoorView(CreateView):
    template_name = 'agmrs_app/agm_indoor/add_agm_indoor.html'
    form_class = AddAgmIndoorForm
    model = AgmDevice
    success_url = reverse_lazy('list_agm_indoor_view')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['active_agm_device'] = 'treeview active'
        context['active_agm_device_add'] = 'active'
        return context

    def form_valid(self, form):
        if form.is_valid():
            print("form valid")
            form.save()
        messages.add_message(self.request, messages.SUCCESS, 'Added Successfully.')
        return super(AddAgmIndoorView, self).form_valid(form)


class ListAgmIndoorView(SingleTableView, FilterView):
    model = AgmDevice
    table = AgmIndoorTable
    template_name = 'agmrs_app/agm_indoor/list_agm_indoor.html'

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        table = self.table(self.get_queryset())
        table.paginate(page=self.request.GET.get('page', 1), per_page=self.paginate_by)
        context['active_agm_device'] = 'treeview active'
        context['active_agm_device_list'] = 'active'
        context['table'] = table
        return context


class EditAgmIndoorView(UpdateView):
    model = AgmDevice
    form_class = EditAgmIndoorForm
    template_name = 'agmrs_app/agm_indoor/edit_agm_indoor.html'

    def get_success_url(self):
        device_id = self.kwargs['device_id']
        return reverse('edit_agm_indoor_view', kwargs={'device_id': self.kwargs['device_id']})

    def form_valid(self, form):
        if form.is_valid():
            print("form is valid")
            form.save()
            messages.add_message(self.request, messages.SUCCESS, "Edited successfully!!")
        return super(EditAgmIndoorView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(EditAgmIndoorView, self).get_context_data(**kwargs)
        context['active_agm_device'] = 'treeview active'
        context['active_agm_device_list'] = 'active'
        return context

    def get_object(self, queryset=None):
        id = self.kwargs['device_id']
        return self.model.objects.get(id=id)


class DeleteAgmIndoorView(DeleteView):
    model = AgmDevice
    template_name = 'agmrs_app/agm_indoor/delete_agm_indoor.html'
    pk_url_kwarg = 'device_id'
    success_url = reverse_lazy('list_agm_indoor_view')
    success_message = "Deleted successfully!!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeleteAgmIndoorView, self).delete(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_agm_device'] = 'treeview active'
        context['active_agm_device_list'] = 'active'
        return context


class AddTeledosimeterView(CreateView):
    template_name = 'agmrs_app/teledosimeter/add_teledosimeter.html'
    form_class = AddTeledosimeterForm
    model = AgmDevice
    success_url = reverse_lazy('list_teledosimeter_view')

    def form_valid(self, form):
        form.instance = TelidosiDevice()
        form.instance.name = form.cleaned_data['name']
        form.instance.device_id = form.cleaned_data['device_id']
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
        context['active_teledosimeter'] = 'treeview active'
        context['active_teledosimeter_add_tele'] = 'active'
        return context


class ListTeledosimeterView(SingleTableView, FilterView):
    model = TelidosiDevice
    table_class = TeledosimeterTable
    template_name = 'agmrs_app/teledosimeter/list_teledosimeter.html'
    context_table_name = 'table'
    paginate_by = 10
    ordering = ['id']

    # filterset_class = EmployeeFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employees'] = AgrmsEmployee.objects.all()
        context['active_teledosimeter'] = 'treeview active'
        context['active_teledosimeter_list_tele'] = 'active'
        return context


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employees'] = AgrmsEmployee.objects.all()
        context['active_teledosimeter'] = 'treeview active'
        context['active_teledosimeter_list_tele'] = 'active'
        return context


class DeleteTeledosimeterView(DeleteView):
    template_name = 'agmrs_app/teledosimeter/delete_teledosimeter.html'
    model = TelidosiDevice
    fields = '__all__'
    pk_url_kwarg = 'device_id'
    success_url = reverse_lazy('list_teledosimeter_view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employees'] = AgrmsEmployee.objects.all()
        context['active_teledosimeter'] = 'treeview active'
        context['active_teledosimeter_list_tele'] = 'active'
        return context


def get_data(request):
    if request.is_ajax() and request.method == 'GET':
        data_id = request.GET.get('id')

        # Fetch data from the database based on the data_id
        try:
            data = AgmDeviceData.objects.get(id=data_id)
            # Process the data as needed

            # Return the data as JSON response
            return JsonResponse({'data': data.some_field})
        except AgmDeviceData.DoesNotExist:
            return JsonResponse({'error': 'Data not found.'})
    else:
        return JsonResponse({'error': 'Invalid request.'})


class AgmIndoorDeviceViewMore(SingleTableView, FilterView):
    model = AgmDeviceData
    table = DevicedataViewMore
    template_name = 'agmrs_app/agm_indoor/device_agm_view_more.html'

    def get_queryset(self):
        device_id = self.kwargs['device']
        return self.model.objects.filter(device__device_id=device_id).order_by('-id')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        table = self.table(self.get_queryset())
        table.paginate(page=self.request.GET.get('page', 1), per_page=self.paginate_by)
        context['active_admin_dash'] = 'treeview active'
        context['table'] = table
        return context


class TeledosiDeviceViewMore(SingleTableView, FilterView):
    model = TelidosiData
    table = TeledosidataViewMore
    template_name = 'agmrs_app/teledosimeter/teledosi_view_more.html'

    def get_queryset(self):
        device_id = self.kwargs['device']
        return self.model.objects.filter(device__device_id=device_id).order_by('-id')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        table = self.table(self.get_queryset())
        table.paginate(page=self.request.GET.get('page', 1), per_page=self.paginate_by)
        context['active_admin_dash'] = 'treeview active'
        context['table'] = table
        return context
