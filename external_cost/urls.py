from django.urls import path
from . import views

urlpatterns = [

	path('add_new',views.add_new,name='add_new'),
	path('external_cost_listing',views.external_cost_listing,name='external_cost_listing'),
	path('update',views.update,name='external_item_update'),
	path('delete',views.delete,name='external_delete'),
	path('stock',views.stock,name='stock_external_cost'),
	path('expense_list',views.expense_list,name='expense_list'),
	path('expense_item',views.expense_item,name='expense_item'),
	path('stock_history',views.stock_history,name='stock_history'),
	path('stock_history_search',views.stock_history_search,name='stock_history_search'),
	path('expense_history',views.expense_history,name='expense_history'),
	path('expense_history_search',views.expense_history_search,name='expense_history_search'),
	path('extra_cost_add',views.extra_cost_add,name='extra_cost_add')


   ]
      