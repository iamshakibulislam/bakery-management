
from django.urls import path
from . import views

urlpatterns = [
   
    path('add_new',views.add_new,name="add_new_raw_material"),
    path('list',views.raw_material_listing,name="raw_material_list"),
    path('update',views.update,name="update"),
    path('delete',views.deleterawmaterial,name='delete_raw_material'),
    path('stock',views.stock,name="raw_material_stock"),
    path('stock/update',views.stock_update,name="stock_update"),
    path('stock/history',views.stock_history,name='raw_stock_history')
]
