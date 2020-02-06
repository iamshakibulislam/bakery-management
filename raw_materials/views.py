from django.shortcuts import render
from .models import *
from django.http import JsonResponse
def add_new(request):
	json={'action':'success'}
	if request.method=="GET":
		item=request.GET['name']
		price=request.GET['price']

		raw_material=raw_material_list()
		raw_material.item=item
		raw_material.price=float(price)
		raw_material.save()
		return JsonResponse(json)



	else:
		json['action']='failed'
		return JsonResponse(json)
