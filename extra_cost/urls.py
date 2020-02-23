from django.urls import path
from . import views

urlpatterns=[
		path('history',views.history,name='extra_cost_history'),
		path('update',views.update,name='update_cost'),
		path('extra_cost_search',views.extra_cost_search,name='extra_cost_search'),
		path('delete',views.extra_cost_delete,name='extra_cost_delete')
]