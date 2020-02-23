from django.shortcuts import render
from .models import *
from extra_cost.models import *
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


#stock 


def stock(request):
	if request.method=="GET":


		item_list=external_cost_list.objects.all()
		stock_list=external_cost_stock.objects.all()

		return render(request,'external_stock_list.html',{'item_list':item_list,'stock_list':stock_list})



		

	if request.method=="POST":
		item=request.POST['item']
		quantity=request.POST['quantity']
		json=[]
		


		if len(external_cost_stock.objects.filter(item__item=item))>0:
			sel_from_list=external_cost_list.objects.get(item=item)

			sel=external_cost_stock.objects.get(item__item=item)
			sel.quantity=float(sel.quantity)+float(quantity)
			sel.value=float(sel.value)+(float(quantity)*float(sel_from_list.price))

			sel.save()
			hist=external_cost_stock_history()
			hist.item=sel_from_list
			hist.quantity=float(quantity)
			hist.save()

			all_obj=external_cost_stock.objects.all()
			for x in all_obj:
				json.append({'id':x.id,'item':x.item.item,'quantity':x.quantity,'value':x.value})

			return JsonResponse(json,safe=False)


		else:
			sel_from_list=external_cost_list.objects.get(item=item)
			stock_table=external_cost_stock()
			stock_table.item=sel_from_list
			stock_table.quantity=float(quantity)
			stock_table.value=float(sel_from_list.price)*float(quantity)
			stock_table.save()
			hist=external_cost_stock_history()
			hist.item=sel_from_list
			hist.quantity=int(quantity)
			hist.save()
			all_obj=external_cost_stock.objects.all()
			for x in all_obj:
				json.append({'id':x.id,'item':x.item.item,'quantity':x.quantity,'value':x.value})

			return JsonResponse(json,safe=False)

			

def expense_list(request):
	json=[]
	ex=external_cost_list.objects.all()
	for x in ex:
		json.append({'item':x.item})

	return JsonResponse(json,safe=False)



def expense_item(request):
	item=request.GET['item']
	quantity=request.GET['quantity']

	stock=external_cost_stock.objects.get(item__item=item)
	sel=external_cost_list.objects.get(item=item)
	expense_table=external_cost_expense()

	stock.quantity=float(stock.quantity)-float(quantity)
	stock.value=(stock.quantity)*(sel.price)
	stock.save()

	expense_table.item=sel
	expense_table.quantity=float(quantity)
	expense_table.value=float(quantity)*float(sel.price)
	expense_table.save()

	return JsonResponse({'status':'ok'})



def stock_history(request):
	hist=external_cost_stock_history.objects.all()[:20]

	return render(request,'external_stock_history.html',{'hist':hist})


def stock_history_search(request):
	fromdate=request.POST['fromdate_external']
	todate=request.POST['todate_external']

	hist=external_cost_stock_history.objects.filter(date__range=[fromdate,todate])

	return render(request,'external_stock_history.html',{'hist':hist})


def expense_history(request):
	hist=external_cost_expense.objects.all()[:15]
	return render(request,'expense_history.html',{'hist':hist})

def expense_history_search(request):
	fromdate=request.POST['fromdate_expense']
	todate=request.POST['todate_expense']

	hist=external_cost_expense.objects.filter(date__range=[fromdate,todate])

	return render(request,'expense_history.html',{'hist':hist})


def extra_cost_add(request):
	if request.method=='GET':
		name=request.GET['name']
		price=request.GET['price']

		inst=extra_cost()
		inst.name=name
		inst.cost=float(price)
		inst.save()
		return JsonResponse({'status':'ok'})