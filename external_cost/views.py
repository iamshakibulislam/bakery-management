from django.shortcuts import render
from .models import *
from django.http import JsonResponse

def add_new(request):
	item=request.GET['item']
	price=float(request.GET['price'])

	instance=external_cost_list()
	instance.item=item
	instance.price=price
	instance.save()

	return JsonResponse({'status':'ok'})


def external_cost_listing(request):
	instance=external_cost_list.objects.all()
	return render(request,'external_cost_list.html',{'items':instance})


def update(request):
	json=[]
	if request.method=="GET":

		item=int(request.GET['itemid'])
		info=external_cost_list.objects.get(id=item)
		name=info.item
		price=info.price

		return JsonResponse({'id':item,'item':name,'price':price})

	if request.method=="POST":

		item=request.POST['item']
		item_id=int(request.POST['item_id'])
		price=request.POST['price']

		inst=external_cost_list.objects.get(id=item_id)
		inst.item=item
		inst.price=price
		inst.save()

		obj=external_cost_list.objects.all()
		for x in obj:
			json.append({'id':x.id,'item':x.item,'price':x.price})

		return JsonResponse(json,safe=False)



def delete(request):
	json=[]
	item_id=int(request.GET['item_id'])
	sel=external_cost_list.objects.get(id=item_id)
	sel.delete()


	obj=external_cost_list.objects.all()
	for x in obj:
		json.append({'id':x.id,'item':x.item,'price':x.price})

	return JsonResponse(json,safe=False)

