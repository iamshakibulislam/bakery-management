"""bakery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
from raw_materials import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('raw_materials/',include('raw_materials.urls')),
    path('production/',include('production.urls')),
    path('sales/',include('sales.urls')),
    path('employee/',include('employee.urls')),
    path('external_cost/',include('external_cost.urls')),
    path('extra_cost/',include('extra_cost.urls')),
    path('login',views.login,name='login'),
    path('profitsearch/',views.profitsearch,name='profitsearch')
]
