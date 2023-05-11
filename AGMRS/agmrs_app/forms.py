from django import forms

from agmrs_app.models import AgrmsEmployee, AgmDevice, TelidosiDevice


class AdminLoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)


class AddEmployeeForm(forms.ModelForm):
    class Meta:
        model = AgrmsEmployee
        fields = ['employee_id', 'name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class EditEmployeeForm(forms.ModelForm):
    class Meta:
        model = AgrmsEmployee
        fields = ['employee_id', 'name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class AddAgmIndoorForm(forms.ModelForm):
    # device_type = forms.ChoiceField(choices=AgmDevice.DEVICE_TYPE_CHOICES)
    class Meta:
        model = AgmDevice
        fields = ['name', 'device_id', 'device_type']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class EditAgmIndoorForm(forms.ModelForm):
    class Meta:
        model = AgmDevice
        fields = ['device_type','name', 'device_id']
    def __init__(self, *args , **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class AddTeledosimeterForm(forms.ModelForm):
    # employee_name = forms.ModelChoiceField(queryset=AgrmsEmployee.objects.all())
    class Meta:
        model = TelidosiDevice
        fields = ['name', 'device_id', 'employee_name']

    def __init__(self, *args , **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class EditTeledosimeterForm(forms.ModelForm):
    class Meta:
        model = TelidosiDevice
        fields = ['name', 'device_id','employee_name']
    def __init__(self, *args , **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'