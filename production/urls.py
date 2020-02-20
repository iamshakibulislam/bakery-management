from django.urls import path
from . import views

urlpatterns = [
   
    path('register',views.register,name="register_product"),
    path('list',views.product_listing,name='product_listing'),
    path('update',views.update,name="update_product"),
    path('delete',views.delete_product,name='delete_product'),
    path('list_raw_mat',views.raw_material_listing,name="raw_material_list_from_production"),
    path('stock',views.stock,name="production_stock"),
    path('stock/update',views.stock_update,name="product_stock_update"),
    path('stock/history',views.stock_history,name="product_stock_history")
   
]
