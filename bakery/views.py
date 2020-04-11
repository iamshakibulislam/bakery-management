from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import *
from raw_materials.models import *
from employee.models import *
from external_cost.models import *
from extra_cost.models import *
from production.models import *
from sales.models import *
import datetime
today=datetime.date.today().strftime("%Y-%m-%d")

def login(request):
	return render(request,'login.html')

def index(request):





	deposit_today_saleman=deposit_from_saleman.objects.filter(date__range=[today,today]).aggregate(s=Sum('amount'))['s']
	if deposit_today_saleman==None:
		deposit_today_saleman=0

	deposit_retail_today=pay_retail.objects.filter(date__range=[today,today]).aggregate(s=Sum('amount'))['s']
	if deposit_retail_today==None:
		deposit_retail_today=0

	todaysdeposit=round(float(deposit_today_saleman+deposit_retail_today),2)

	raw_materials=raw_material_list.objects.all()
	total_raw_stock_value=raw_material_stock.objects.all().aggregate(s=Sum('value'))['s']
	if total_raw_stock_value==None:
		total_raw_stock_value=0
	product_Stock=product_stock.objects.all().aggregate(s=Sum('value'))['s']
	if product_Stock==None:
		product_Stock=0
	external_stock=external_cost_stock.objects.all().aggregate(s=Sum('value'))['s']
	if external_stock==None:
		external_stock=0

	saleman_aftcom_value=saleman_sale.objects.all().aggregate(s=Sum('after_commission_value'))['s']
	if saleman_aftcom_value==None:
		saleman_aftcom_value=0
	saleman_deposit=deposit_from_saleman.objects.all().aggregate(s=Sum('amount'))['s']
	if saleman_deposit==None:
		saleman_deposit=0

	total_saleman_due=round(float(saleman_aftcom_value-saleman_deposit),3)

	retail_value=retail.objects.all().aggregate(s=Sum('value'))['s']
	if retail_value==None:
		retail_value=0
	retail_pay=pay_retail.objects.all().aggregate(s=Sum('amount'))['s']
	if retail_pay==None:
		retail_pay=0

	retail_due=round(float(retail_value-retail_pay))

	total_due=round(float(total_saleman_due+retail_due),3)

	todays_extra_cost=extra_cost.objects.filter(date__range=[today,today]).aggregate(s=Sum('cost'))['s']

	if todays_extra_cost==None:
		todays_extra_cost=0

	

	attend_value=attendence.objects.all().aggregate(s=Sum('add_salary'))['s']

	if attend_value==None:
		attend_value=0

	paid_emp=pay_employee.objects.all().aggregate(s=Sum('amount'))['s']
	if paid_emp==None:
		paid_emp=0



	employee_due=round(float(attend_value-paid_emp),3)
	
	


	context={'raw_materials':raw_materials,'raw_stock':total_raw_stock_value,'product_Stock':product_Stock,'external_stock':external_stock,

				'saleman_due':total_saleman_due,'retail_due':retail_due,'total_due':total_due,'todays_extra_cost':todays_extra_cost,
				'employee_due':employee_due,'todaysdeposit':todaysdeposit
				

	            }

	return render(request,'index.html',context)




def profitsearch(request):
	from_date=request.GET['fromdate']
	to_date=request.GET['todate']

	json=[]


	raw_mat_total=product_stock_history.objects.filter(date__range=[from_date,to_date]).aggregate(s=Sum('raw_mat_value'))['s']
	if raw_mat_total==None:
		raw_mat_total=0
	
	external_cost_expense_total=external_cost_expense.objects.filter(date__range=[from_date,to_date]).aggregate(s=Sum('value'))['s']
	if external_cost_expense_total==None:
		external_cost_expense_total=0
	
	salary_total=attendence.objects.filter(date__range=[from_date,to_date]).aggregate(s=Sum('add_salary'))['s']
	if salary_total==None:
		salary_total=0

	extracost_total=extra_cost.objects.filter(date__range=[from_date,to_date]).aggregate(s=Sum('cost'))['s']
	if extracost_total==None:
		extracost_total=0


	deposit_total_saleman=deposit_from_saleman.objects.filter(date__range=[from_date,to_date]).aggregate(s=Sum('amount'))['s']
	if deposit_total_saleman==None:
		deposit_total_saleman=0

	deposit_retail_total=pay_retail.objects.filter(date__range=[from_date,to_date]).aggregate(s=Sum('amount'))['s']
	if deposit_retail_total==None:
		deposit_retail_total=0

	expense=round(float(raw_mat_total+external_cost_expense_total+salary_total+extracost_total),2)
	deposit=round(float(deposit_total_saleman+deposit_retail_total),2)

	profit=round((deposit-expense),2)
	json.append({'profit':profit})




	return JsonResponse(json,safe=False)