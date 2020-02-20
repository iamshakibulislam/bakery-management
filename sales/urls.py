from django.urls import path
from . import views
from sales import urls

urlpatterns = [
    path('new_saleman',views.new_saleman,name='new_saleman'),
    path('saleman_list',views.saleman_list_show,name='saleman_list'),
    path('saleman/update',views.saleman_update,name='saleman_update'),
    path('saleman/delete',views.saleman_delete,name='saleman_delete'),
    path('saleman/sale',views.saleman_sell,name='saleman_sale'),
    path('saleman/sold',views.saleman_sold,name='soldtosaleman'),
    path('retail_sales',views.retail_sale,name='retail_sales'),
    path('retail/sold',views.retail_sell,name='retail_sold'),
    path('retail/status',views.retail_status,name='retail_status'),
    path('delete/retail',views.delete_retail,name='delete_retail'),
    path('retail_search',views.retail_search,name='retail_search'),
    path('saleman_profile/<int:saleman_id>',views.saleman_profile,name='saleman_profile'),
    path('saleman_profile/search',views.saleman_profile_search,name='saleman_profile_search'),
    path('saleman_deposit',views.saleman_deposit,name='saleman_deposit'),
    path('retail_search_facility',views.retail_search_facility,name='retail_search_facility'),
    path('retail_due_history',views.retail_due_history,name='retail_due_history'),
    path('retail_deposit',views.retail_deposit,name='retail_deposit')
]