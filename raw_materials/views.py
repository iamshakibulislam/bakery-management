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



def raw_material_listing(request):
	raw_materials=raw_material_list.objects.all()
	return render(request,'raw_material_list.html',{'raw_materials':raw_materials})


def update(request):
	json={}
	all_list=[]
	if request.method=="GET":
		raw_material=request.GET['raw_material']
		info=raw_material_list.objects.get(id=int(raw_material))
		json['id']=info.id
		json['item']=info.item
		json['price']=info.price

		return JsonResponse(json)


	
	else:
		raw_material_id=request.POST['item_id']
		raw_material_name=request.POST['item']
		raw_material_price=request.POST['price']

		select=raw_material_list.objects.get(id=int(raw_material_id))
		select.item=raw_material_name
		select.price=raw_material_price
		select.save()
		allobj=raw_material_list.objects.all()
		for x in allobj:

			itemid=x.id
			item=x.item
			price=x.price
			all_list.append({'id':itemid,'item':item,'price':price})
		




		return JsonResponse(all_list,safe=False)

def deleterawmaterial(request):
	all_list=[]
	if request.method=="GET":
		matid=request.GET['material_id']
		select=raw_material_list.objects.get(id=int(matid))
		select.delete()
		a=raw_material_list.objects.all()

		for x in a:

			itemid=x.id
			item=x.item
			price=x.price
			all_list.append({'id':itemid,'item':item,'price':price})
		

		return JsonResponse(all_list,safe=False)



def stock(request):
	if request.method=="GET":


		item_list=raw_material_list.objects.all()
		stock_list=raw_material_stock.objects.all()

		return render(request,'add_raw_material_to_stock.html',{'item_list':item_list,'stock_list':stock_list})

	if request.method=="POST":
		item=request.POST['item']
		quantity=request.POST['quantity']
		json=[]
		


		if len(raw_material_stock.objects.filter(item__item=item))>0:
			sel_from_list=raw_material_list.objects.get(item=item)
			sel=raw_material_stock.objects.get(item__item=item)
			sel.quantity=int(sel.quantity)+int(quantity)
			sel.value=float(sel.value)+(int(quantity)*float(sel_from_list.price))
			sel.save()
			hist=raw_material_stock_history()
			hist.item=sel_from_list
			hist.quantity=int(quantity)
			hist.save()

			all_obj=raw_material_stock.objects.all()
			for x in all_obj:
				json.append({'id':x.id,'item':x.item.item,'quantity':x.quantity,'value':x.value})

			return JsonResponse(json,safe=False)


		else:
			sel_from_list=raw_material_list.objects.get(item=item)
			stock_table=raw_material_stock()
			stock_table.item=sel_from_list
			stock_table.quantity=int(quantity)
			stock_table.value=int(sel_from_list.price)*int(quantity)
			stock_table.save()
			hist=raw_material_stock_history()
			hist.item=sel_from_list
			hist.quantity=int(quantity)
			hist.save()
			all_obj=raw_material_stock.objects.all()
			for x in all_obj:
				json.append({'id':x.id,'item':x.item.item,'quantity':x.quantity,'value':x.value})

			return JsonResponse(json,safe=False)


def stock_update(request):
	json=[]
	if request.method=="GET":
		stock_id=request.GET['stock_material']
		select_stock=raw_material_stock.objects.get(id=int(stock_id))
		return JsonResponse({'id':select_stock.id,'item':select_stock.item.item,'quantity':select_stock.quantity,'value':select_stock.value})

	elif request.method=="POST":
		item=request.POST['item']
		quantity=int(request.POST['quantity'])
		value=int(request.POST['value'])
		item_id=int(request.POST['item_id'])

		sl=raw_material_stock.objects.get(id=item_id)
		sl.quantity=quantity
		sl.value=value
		sl.save()


		hist=raw_material_stock_history()

		hist.item=raw_material_list.objects.get(item=item)
		hist.quantity=quantity
		hist.save()
		all_obj=raw_material_stock.objects.all()
		for x in all_obj:
			json.append({'id':x.id,'item':x.item.item,'quantity':x.quantity,'value':x.value})


		return JsonResponse(json,safe=False)




def stock_history(request):
	json=[]
	if request.method=="GET":
		his=raw_material_stock_history.objects.all()[:10]
		return render(request,'raw_material_stock_history.html',{'history':his})



	if request.method=="POST":
		from_date=request.POST['from']
		to_date=request.POST['to']

		filtered_history=raw_material_stock_history.objects.filter(date__range=[from_date,to_date])
		for x in filtered_history:
			json.append({'date':str(x.date),'item':str(x.item),'quantity':str(x.quantity)})
		return JsonResponse(json,safe=False)

		'''for item in filtered_history:
			json.append({'date':item.date,'item':item.item,'quantity':item.quantity})

		return JsonResponse(json,safe=False)'''






			


