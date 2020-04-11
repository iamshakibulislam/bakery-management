from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponseRedirect
from sales.models import *
from production.models import *
from django.db.models import *
import json


def new_saleman(request):
	name=request.GET['name']
	mobile=request.GET['mobile']
	commission=request.GET['commission']

	salemanlist=saleman_list()
	salemanlist.name=name
	salemanlist.mobile=mobile
	salemanlist.commission=commission
	salemanlist.save()

	return JsonResponse({'status':'ok'})



def saleman_list_show(request):
	obj=saleman_list.objects.all()
	return render(request,'saleman_list.html',{'list':obj})





def saleman_update(request):
	json={}
	all_list=[]
	if request.method=="GET":
		saleman=request.GET['saleman']
		info=saleman_list.objects.get(id=int(saleman))
		json['id']=info.id
		json['name']=info.name
		json['commission']=info.commission
		json['mobile']=info.mobile

		return JsonResponse(json)

   
	
	else:
		saleman_id=request.POST['saleman_id']
		saleman_name=request.POST['name']
		saleman_mobile=request.POST['mobile']
		saleman_commission=request.POST['commission']

		select=saleman_list.objects.get(id=int(saleman_id))
		select.name=saleman_name
		select.mobile=saleman_mobile
		select.commission=saleman_commission
		select.save()
		allobj=saleman_list.objects.all()
		for x in allobj:

			salemanid=x.id
			name=x.name
			commission=x.commission
			all_list.append({'id':salemanid,'name':name,'commission':commission})
		




		return JsonResponse(all_list,safe=False)







def saleman_delete(request):
	all_list=[]
	if request.method=="GET":
		proid=request.GET['saleman_id']
		select=saleman_list.objects.get(id=int(proid))
		select.delete()
		a=saleman_list.objects.all()

		for x in a:

			salemanid=x.id
			name=x.name
			commission=x.commission
			all_list.append({'id':salemanid,'name':name,'commission':commission})
		

		return JsonResponse(all_list,safe=False)


def saleman_sell(request):
	salemanlist=saleman_list.objects.all()
	productlist=product_list.objects.all()
	context={'saleman':salemanlist,'product':productlist}
	return render(request,'sell_to_salesman.html',context)


def saleman_sold(request):
	data=request.GET['saledata']
	saleman=request.GET['saleman']

	product_data=json.loads(data)
	saleman_name=json.loads(saleman)['name']

	salemanname=saleman_list.objects.get(name=saleman_name)

	for data in product_data:
		product_name=data['product']
		product_quantity=int(data['quantity'])

		productname=product_list.objects.get(name=product_name)
		productvalue=product_quantity*(float(productname.price))
		after_commission_value=productvalue-(productvalue*((float(salemanname.commission))/100))

		stock_product=product_stock.objects.get(name__name=product_name)
		stock_product.quantity=(stock_product.quantity)-product_quantity
		stock_product.value=(stock_product.quantity)*(productname.price)
		stock_product.save()



		sale_table=saleman_sale()
		sale_table.name=salemanname
		sale_table.product=productname
		sale_table.quantity=product_quantity
		sale_table.value=productvalue
		sale_table.after_commission_value=after_commission_value
		sale_table.save()





	return JsonResponse({'status':'ok'})
		



def retail_sale(request):
	retailers=retail_sales.objects.all()[:20]
	product=product_list.objects.all()
	return render(request,'retail_sales.html',{'retailers':retailers,'product':product})


def retail_sell(request):
	saledata=request.GET['saledata']
	retailer=request.GET['retailer']

	sale_data=json.loads(saledata)
	retailer_name=json.loads(retailer)['name']


	try:
		retail_sales.objects.get(name=retailer_name)

	except:
		retail_table=retail_sales()
		retail_table.name=retailer_name
		retail_table.save()

	sel_retailer=retail_sales.objects.get(name=retailer_name)


	for data in sale_data:
		product_name=data['product']
		product_quantity=int(data['quantity'])

		productname=product_list.objects.get(name=product_name)
		productvalue=product_quantity*(float(productname.price))
		

		stock_product=product_stock.objects.get(name__name=product_name)
		stock_product.quantity=(stock_product.quantity)-product_quantity
		stock_product.value=(stock_product.quantity)*(productname.price)
		stock_product.save()

		retail_through_table=retail()
		retail_through_table.name=sel_retailer
		retail_through_table.quantity=product_quantity
		retail_through_table.product=productname
		retail_through_table.value=productvalue
		retail_through_table.save()

	return JsonResponse({'status':'ok'})




def retail_status(request):
	retailer=retail_sales.objects.all()[:20]
	return render(request,'retail_sales_status.html',{'names':retailer})


def delete_retail(request):
	json=[]
	if request.method=="GET":
		idretail=int(request.GET['id'])


		select=retail_sales.objects.get(id=idretail)
		select.delete()

		obj=retail_sales.objects.all()

		for x in obj:
			idnum=x.id
			name=x.name
			json.append({'id':idnum,'name':name})

		print(json)

		return JsonResponse({'status':'ok'})




def retail_search(request):
	if request.method=='GET':
		fromdate=request.GET['from_date']
		todate=request.GET['to_date']

		sel=retail_sales.objects.filter(date__range=[fromdate,todate])
		
		context={'names':sel}
		return render(request,'retail_sales_status.html',context)


def saleman_profile(request,saleman_id):
	name=saleman_list.objects.get(id=saleman_id).name
	alldue=saleman_sale.objects.filter(name_id=saleman_id).aggregate(due=Sum('after_commission_value'))['due']
	if alldue==None:
		alldue=0
	
	deposit=deposit_from_saleman.objects.filter(name_id=saleman_id).aggregate(deposit=Sum('amount'))['deposit']
	if deposit==None:
		deposit=0
	total_due=alldue-deposit
	lastsellinghist=saleman_sale.objects.filter(name_id=saleman_id)[:20]
	
	
	return render(request,'saleman_profile.html',{'name':name,'totaldue':total_due,'selected_value':0,'sale_list':lastsellinghist,'id':saleman_id,'selected_due':0})



def saleman_profile_search(request):
	
	if request.method=="POST":

		fromdate=request.POST['from_date_profile']
		todate=request.POST['to_date_profile']
		saleman=int(request.POST['saleman_id'])
		datefilter=saleman_sale.objects.filter(name_id=saleman,date__range=[fromdate,todate])
		selected_aftcomtotal=datefilter.aggregate(aft_com_total=Sum('after_commission_value'))['aft_com_total']
		if selected_aftcomtotal==None:
			selected_aftcomtotal=0
		sel_deposit=deposit_from_saleman.objects.filter(name_id=saleman,date__range=[fromdate,todate]).aggregate(seldeposit=Sum('amount'))['seldeposit']
		if sel_deposit==None:
			sel_deposit=0
		selected_due=selected_aftcomtotal-sel_deposit


		alldue=saleman_sale.objects.filter(name_id=saleman).aggregate(due=Sum('after_commission_value'))['due']
		if alldue==None:
			alldue=0
	
		deposit=deposit_from_saleman.objects.filter(name_id=saleman).aggregate(deposit=Sum('amount'))['deposit']
		if deposit==None:
			deposit=0
		total_due=alldue-deposit
		sel_value=datefilter.aggregate(selvalue=Sum('value'))['selvalue']
		name=saleman_list.objects.get(id=saleman).name

		return render(request,'saleman_profile.html',{'name':name,'totaldue':total_due,'selected_due':selected_due,'sale_list':datefilter,'id':saleman,'selected_value':sel_value})

	


def saleman_deposit(request):
	if request.method=="POST":

		amount=int(request.POST['amount'])
		saleman=request.POST['salemanname']
		identity=str(request.POST['id'])

		sale_man=saleman_list.objects.get(name=saleman)

		deposit=deposit_from_saleman()
		deposit.name=sale_man
		deposit.amount=amount
		deposit.save()
		redir='/sales/saleman_profile/'+identity
		return HttpResponseRedirect(redir)







def retail_search_facility(request):
	json=[]
	if request.method=='GET':
		name=request.GET['name']
		retailers=retail_sales.objects.filter(name__icontains=name)
		for retailer in retailers:
			json.append({'name':retailer.name})
		return JsonResponse(json,safe=False)



def retail_due_history(request):
	json=[]
	if request.method=="GET":
		name=request.GET['name']
		sel=retail_sales.objects.get(name=name)
		allsel=retail.objects.filter(name=sel)
		totalvalue=allsel.aggregate(tvalue=Sum('value'))['tvalue']
		if totalvalue==None:
			totalvalue=0

		joma=pay_retail.objects.filter(name=sel)

		tjoma=joma.aggregate(j=Sum('amount'))['j']
		if tjoma==None:
			tjoma=0

		totaldue=totalvalue-tjoma

		for date,product,quantity,value in allsel.values_list('date','product','quantity','value'):
			productname=product_list.objects.get(id=product).name
			json.append({'date':date,'product':productname,'quantity':quantity,'value':value})


		json.append({'total_due':totaldue})



		return JsonResponse(json,safe=False)



def retail_deposit(request):
	amount=request.GET['amount']
	name=request.GET['name']

	selname=retail_sales.objects.get(name=name)
	pay=pay_retail()
	pay.name=selname
	pay.amount=amount
	pay.save()

	return JsonResponse({'status':'ok'})