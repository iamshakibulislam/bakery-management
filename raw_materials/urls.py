
from django.urls import path
from . import views

urlpatterns = [
   
    path('add_new',views.add_new,name="add_new_raw_material")
]
