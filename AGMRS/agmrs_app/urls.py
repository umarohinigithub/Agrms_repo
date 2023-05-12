from django.urls import path

from agmrs_app.views import TestTemplateView, AdminDashBoardView, AgmIndoorView, AgmOutdoorView, AdminLoginView, \
    AdminLogoutView, TeledosiView, AddEmployeeView, ListEmployeeView, EditEmployeeView, DeleteEmployeeView, \
    AddAgmIndoorView, ListAgmIndoorView, EditAgmIndoorView, AddTeledosimeterView, ListTeledosimeterView, \
    EditTeledosimeterView, DeleteAgmIndoorView, DeleteTeledosimeterView, get_current_data_outdoor, \
    get_current_data_indoor, get_data, AgmIndoorDeviceViewMore

urlpatterns = [
    # path('', AdminDashboardView.as_view(), name='admin_dashboard_view'),
    path('', AdminLoginView.as_view(), name='admin_login_view'),
    path('dashboard/', AdminDashBoardView.as_view(), name='dashboard_view'),
    path('logout/', AdminLogoutView.as_view(), name='admin_logout_view'),
    path('test/', TestTemplateView.as_view(), name='agmrs_sensor_view'),
    path('agm_indoor/', AgmIndoorView.as_view(), name='agm_indoor_view'),
    path('agm_outdoor/', AgmOutdoorView.as_view(), name='agm_outdoor_view'),
    path('teledosimeter/', TeledosiView.as_view(), name='teledosi_view'),

    ##Employee
    path('employee/add/',AddEmployeeView.as_view(), name ='add_employee_view'),
    path('employee/list/',ListEmployeeView.as_view(), name ='list_employee_view'),
    path('employee/edit<int:employee_id>/',EditEmployeeView.as_view(), name ='edit_employee_view'),
    path('employee/delete<int:employee_id>/',DeleteEmployeeView.as_view(), name ='delete_employee_view'),

    ##AGM Indoor
    path('agm_device/add/',AddAgmIndoorView.as_view(), name ='add_agm_indoor_view'),
    path('agm_device/list/',ListAgmIndoorView.as_view(), name ='list_agm_indoor_view'),
    path('agm_device/edit<int:device_id>/',EditAgmIndoorView.as_view(), name ='edit_agm_indoor_view'),
    path('agm_device/delete<int:device_id>/',DeleteAgmIndoorView.as_view(), name ='delete_agm_indoor_view'),

     ##Teledosimeter
     path('teledosimeter/add/', AddTeledosimeterView.as_view(), name='add_teledosimeter_view'),
     path('teledosimeter/list/', ListTeledosimeterView.as_view(), name='list_teledosimeter_view'),
     path('teledosimeter/edit<int:device_id>/', EditTeledosimeterView.as_view(), name='edit_teledosimeter_view'),
     path('teledosimeter/delete<int:device_id>/',DeleteTeledosimeterView.as_view(), name ='delete_teledosimeter_view'),

    path('get-current-data-outdoor/', get_current_data_outdoor, name='get_current_data_outdoor'),
    path('get-current-data-indoor/', get_current_data_indoor, name='get_current_data_indoor'),

    path('agm_device/view-more/<int:device>/', AgmIndoorDeviceViewMore.as_view(), name='indoor_device_data_view_more'),

]
