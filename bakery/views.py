from django.shortcuts import render
from raw_materials.models import raw_material_list

def index(request):
	raw_materials=raw_material_list.objects.all()
	return render(request,'index.html',{'raw_materials':raw_materials})