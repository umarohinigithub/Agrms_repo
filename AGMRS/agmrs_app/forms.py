from django import forms

from agmrs_app.models import AgrmsEmployee, AgmDevice, TelidosiDevice


class AdminLoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)


class AddEmployeeForm(forms.ModelForm):
    class Meta:
        model = AgrmsEmployee
        fields = ['employee_id', 'name']


class EditEmployeeForm(forms.ModelForm):
    class Meta:
        model = AgrmsEmployee
        fields = ['employee_id', 'name']


class AddAgmIndoorForm(forms.ModelForm):
    # device_type = forms.ChoiceField(choices=AgmDevice.DEVICE_TYPE_CHOICES)
    class Meta:
        model = AgmDevice
        fields = ['name', 'device_id', 'location', 'present_value', 'average_value', 'battery_percentage', 'device_type']


class EditAgmIndoorForm(forms.ModelForm):
    class Meta:
        model = AgmDevice
        fields = ['device_type','name', 'device_id', 'location', 'present_value', 'average_value', 'battery_percentage']


class AddTeledosimeterForm(forms.ModelForm):
    employee_name = forms.ModelChoiceField(queryset=AgrmsEmployee.objects.all())
    class Meta:
        model = TelidosiDevice
        fields = ['name', 'device_id', 'employee_name', 'total_dose', 'count']


class EditTeledosimeterForm(forms.ModelForm):
    class Meta:
        model = TelidosiDevice
        fields = ['name', 'device_id','employee_name', 'total_dose', 'count']
