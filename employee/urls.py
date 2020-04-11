from django.urls import path,include
from . import views


urlpatterns=[

path('add',views.add_new,name='add_new_employee'),
path('employee_list',views.employee_listing,name='employee_list'),
path('update',views.update,name='update_employee'),
path('delete',views.delete,name='delete_employee'),
path('attendence',views.employee_attendence,name='attendence'),
path('attend',views.attend,name='attend'),
path('employee_details',views.employee_details,name='employee_details'),
path('pay_employees',views.pay_employees,name='pay_employees'),
path('search_employee',views.search_employee,name='search_employee')


]