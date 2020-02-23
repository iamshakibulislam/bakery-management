from django.shortcuts import render
from django.http import JsonResponse
import json
from raw_materials.models import *

from .models import *


def register(request):
	if request.method=='POST':
		item_list=request.POST['item_list']
		
		product=request.POST['product']
		price=int(request.POST['price'])
		try:

			prod_entry=product_list()
			prod_entry.name=product
			prod_entry.price=price
			prod_entry.save()
		except:
			raise ValueError

		b=json.loads(item_list)
		sl_product=product_list.objects.get(name=product)
		for x in b:
			
			
			sl_rawmat=raw_material_list.objects.get(item=x['item'])
			
			quantity=int(x['quantity'])
			through_table=product_rawmaterial()
			through_table.quantity=quantity
			through_table.material=sl_rawmat
			through_table.product=sl_product
			through_table.save()
		return JsonResponse({'status':'ok'})

def raw_material_listing(request):
	main=[]
	product=[]
	json=[]
	if request.method=="GET":
		allobj=raw_material_list.objects.all()
		for x in allobj:
			json.append({'item':x.item})
		for pro in product_list.objects.all():
			product.append({'product':pro.name})
		main.append(json)
		main.append(product)

		return JsonResponse(main,safe=False)



def product_listing(request):
	obj=product_list.objects.all()
	return render(request,'product_list.html',{'product':obj})



def update(request):
	json={}
	all_list=[]
	if request.method=="GET":
		product=request.GET['product_id']
		info=product_list.objects.get(id=int(product))
		json['id']=info.id
		json['item']=info.name
		json['price']=info.price

		return JsonResponse(json)


	
	else:
		product_id=request.POST['item_id']
		product_name=request.POST['item']
		product_price=request.POST['price']

		select=product_list.objects.get(id=int(product_id))
		select.name=product_name
		select.price=product_price
		select.save()
		allobj=product_list.objects.all()
		for x in allobj:

			itemid=x.id
			item=x.name
			price=x.price
			all_list.append({'id':itemid,'item':item,'price':price})
		




		return JsonResponse(all_list,safe=False)




def delete_product(request):
	all_list=[]
	if request.method=="GET":
		proid=request.GET['product_id']
		select=product_list.objects.get(id=int(proid))
		select.delete()
		a=product_list.objects.all()

		for x in a:

			itemid=x.id
			item=x.name
			price=x.price
			all_list.append({'id':itemid,'item':item,'price':price})
		

		return JsonResponse(all_list,safe=False)
		
							
#adding item to stock


def stock(request):
	if request.method=="GET":


		item_list=product_list.objects.all()
		stock_list=product_stock.objects.all()

		return render(request,'product-stock.html',{'item_list':item_list,'stock_list':stock_list})
	

	if request.method=="POST":
		item=request.POST['item']
		quantity=request.POST['quantity']
		json=[]
		


		if len(product_stock.objects.filter(name__name=item))>0:
			sel_from_list=product_list.objects.get(name=item)
			all_mat_for_this=product_rawmaterial.objects.filter(product_id=sel_from_list.id)
			details=all_mat_for_this.values_list('id','material_id','quantity')
			for i,mat,quan in details:
				sel_list=raw_material_list.objects.get(id=mat)

				
				sel_raw_stock=raw_material_stock.objects.get(item_id=mat)
				sel_raw_stock.quantity=round(float(sel_raw_stock.quantity)-((float(quan)*int(quantity))/1000),3)
				sel_raw_stock.value=round((sel_raw_stock.quantity)*(sel_list.price),3)
				sel_raw_stock.save()
				



			sel=product_stock.objects.get(name__name=item)
			sel.quantity=int(sel.quantity)+int(quantity)
			sel.value=float(sel.value)+(int(quantity)*float(sel_from_list.price))
			sel.save()
			hist=product_stock_history()
			hist.name=sel_from_list
			hist.quantity=int(quantity)
			hist.save()

			all_obj=product_stock.objects.all()
			for x in all_obj:
				json.append({'id':x.id,'item':x.name.name,'quantity':x.quantity,'value':x.value})

			return JsonResponse(json,safe=False)


		else:
			sel_from_list=product_list.objects.get(name=item)
			all_mat_for_this=product_rawmaterial.objects.filter(product_id=sel_from_list.id)
			details=all_mat_for_this.values_list('id','material_id','quantity')
			for i,mat,quan in details:
				sel_list=raw_material_list.objects.get(id=mat)

				
				sel_raw_stock=raw_material_stock.objects.get(item_id=mat)
				sel_raw_stock.quantity=round(float(sel_raw_stock.quantity)-((float(quan)*int(quantity))/1000),3)
				sel_raw_stock.value=round((sel_raw_stock.quantity)*(sel_list.price),3)
				sel_raw_stock.save()




			stock_table=product_stock()
			stock_table.name=sel_from_list
			stock_table.quantity=int(quantity)
			stock_table.value=int(sel_from_list.price)*int(quantity)
			stock_table.save()
			hist=product_stock_history()
			hist.name=sel_from_list
			hist.quantity=int(quantity)
			hist.save()
			all_obj=product_stock.objects.all()
			for x in all_obj:
				json.append({'id':x.id,'item':x.name.name,'quantity':x.quantity,'value':x.value})

			return JsonResponse(json,safe=False)







def stock_update(request):
	json=[]
	if request.method=="GET":
		stock_id=request.GET['product']
		select_stock=product_stock.objects.get(id=int(stock_id))
		return JsonResponse({'id':select_stock.id,'item':select_stock.name.name,'quantity':select_stock.quantity,'value':select_stock.value})
'''
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
'''
			



def stock_history(request):



	json=[]
	if request.method=="GET":
		his=product_stock_history.objects.all()[:10]
		return render(request,'product_stock_history.html',{'history':his})



	if request.method=="POST":
		from_date=request.POST['from']
		to_date=request.POST['to']

		filtered_history=product_stock_history.objects.filter(date__range=[from_date,to_date])
		for x in filtered_history:
			json.append({'date':str(x.date),'item':str(x.name.name),'quantity':str(x.quantity)})
		return JsonResponse(json,safe=False)