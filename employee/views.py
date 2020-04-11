from django.shortcuts import render
from django.http import JsonResponse,HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import *
from .models import *
# Create your views here.
today=datetime.date.today().strftime("%Y-%m-%d")
def add_new(request):
	name=request.GET['name']
	salary=request.GET['salary']
	employee_table=employee_list()
	employee_table.name=name
	employee_table.salary=salary
	employee_table.save()

	return JsonResponse({'status':'ok'})



def employee_listing(request):
	employees=employee_list.objects.all()
	return render(request,'employee_list.html',{'employee':employees})

def update(request):
	if request.method=="GET":


		json=[]
		employee_id=request.GET['employee_id']
		obj=employee_list.objects.get(id=int(employee_id))
		json.append({'id':obj.id,'name':obj.name,'salary':obj.salary})
		return JsonResponse(json,safe=False)



	if request.method=="POST":
		response=[]
		emp_id=request.POST['employee_id']
		name=request.POST['name']
		salary=request.POST['salary']

		emp=employee_list.objects.get(id=int(emp_id))
		emp.name=name
		emp.salary=salary
		emp.save()

		all_emp=employee_list.objects.all()
		for x in all_emp:
			response.append({'id':x.id,'name':x.name,'salary':x.salary})

		return JsonResponse(response,safe=False)


def delete(request):
	json=[]
	if request.method=="GET":
		empid=request.GET['employee_id']

		empsel=employee_list.objects.get(id=int(empid))
		empsel.delete()

		allobj=employee_list.objects.all()

		for x in allobj:
			json.append({'id':x.id,'name':x.name,'salary':x.salary})

		return JsonResponse(json,safe=False)



def employee_attendence(request):
	emp_list_with_status=[]
	emplist=employee_list.objects.all()

	for emp in emplist:
		status=''
		Id=emp.id
		
		sel=employee_list.objects.get(id=Id)

		try:
			findtoday=attendence.objects.get(date=today,name=sel)
			status='yes'
		except ObjectDoesNotExist:
			status='no'
		name=emp.name
		emp_list_with_status.append({'name':name,'id':Id,'status':status})
	

		


	return render(request,'employee_attendence.html',{'attend':emp_list_with_status})



def attend(request):
	if request.method=="GET":
		emp_id=request.GET['id']
		sel=employee_list.objects.get(id=int(emp_id))
		salary=sel.salary
		try:
			hajira=attendence.objects.get(date=today,name=sel)
			hajira.delete()

		except:
			att=attendence()
			att.name=sel
			att.status=True
			att.add_salary=(float(salary)/30)
			att.save()


	return JsonResponse({'status':'ok'})





def employee_details(request):
	json=[]
	attending=[]
	info=[]
	employee_id=request.GET['id']

	sel=employee_list.objects.get(id=int(employee_id))
	name=sel.name

	sum_of_workingdays=attendence.objects.filter(name=sel).aggregate(due=Sum('add_salary'))['due']
	if sum_of_workingdays==None:
		sum_of_workingdays=0

	paidemployee=pay_employee.objects.filter(name=sel).aggregate(paid=Sum('amount'))['paid']
	if paidemployee==None:
		paidemployee=0
	

	total_due=float(sum_of_workingdays)-float(paidemployee)
	info.append({'name':name,'total_due':total_due})

	presence=attendence.objects.filter(name=sel)[:10]
	for x in presence:
		date=x.date
		attending.append({'date':date})

	json.append(attending)
	json.append(info)


	return JsonResponse(json,safe=False)
	

	
def pay_employees(request):
	if request.method=="GET":
		employee=request.GET['name']
		amount=request.GET['amount']

		sel=employee_list.objects.get(name=employee)

		pay=pay_employee()
		pay.name=sel
		pay.amount=float(amount)
		pay.save()

		return JsonResponse({'status':'ok'})




def search_employee(request):
	json=[]
	fromdate=request.GET['from']
	todate=request.GET['to']

	name=request.GET['name']

	sel=employee_list.objects.get(name=name)
	selall=attendence.objects.filter(name=sel,date__range=[fromdate,todate])

	for x in selall:
		json.append({'date':x.date})



	return JsonResponse(json,safe=False)