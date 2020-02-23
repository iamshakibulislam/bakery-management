from django.shortcuts import render
from .models import *
from django.http import JsonResponse
# Create your views here.
def history(request):
	obj=extra_cost.objects.all()[:15]
	return render(request,'cost_history.html',{'cost_history':obj})


def update(request):
	if request.method=="GET":

		json=[]
		cost_id=int(request.GET['costid'])

		costsel=extra_cost.objects.get(id=cost_id)
		json.append({'id':costsel.id,'name':costsel.name,'amount':costsel.cost})


		return JsonResponse(json,safe=False)

	if request.method=="POST":
		data=[]
		fromd=''
		tod=''
		try:
			fromdate=request.POST['fromdate']
			fromd=fromdate
		except:
			fromd=0

		try:
			todate=request.POST['todate']
			tod=todate
		except:
			tod=0

		
		name=request.POST['name']
		amount=request.POST['amount']
		cost_id=request.POST['cost_id']
		costselection=extra_cost.objects.get(id=int(cost_id))
		costselection.name=name
		costselection.cost=amount
		costselection.save()
		if fromd==0 or tod==0:

			allobj=extra_cost.objects.all()[:15]
			for x in allobj:
				data.append({'id':x.id,'name':x.name,'amount':x.cost,'date':x.date})
		else:
			allobj=extra_cost.objects.filter(date__range=[fromd,tod])
			for x in allobj:
				data.append({'id':x.id,'name':x.name,'amount':x.cost,'date':x.date})



		return JsonResponse(data,safe=False)



def extra_cost_search(request):
	if request.method=="GET":
		fromdate=request.GET['fromdate_extracost']
		todate=request.GET['todate_extracost']

		filtered=extra_cost.objects.filter(date__range=[fromdate,todate])
		return render(request,'cost_history.html',{'cost_history':filtered})


def extra_cost_delete(request):
	if request.method=="GET":
		cost=int(request.GET['cost_id'])
		extra_cost.objects.get(id=cost).delete()
		return JsonResponse({'status':'ok'})



