from django.urls import path
from . import views

urlpatterns = [

	path('add_new',views.add_new,name='add_new'),
	path('external_cost_listing',views.external_cost_listing,name='external_cost_listing'),
	path('update',views.update,name='external_item_update'),
	path('delete',views.delete,name='external_delete')


   ]
      