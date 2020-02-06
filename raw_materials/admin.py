from django.contrib import admin

# Register your models here.
from .models import raw_material_list,raw_material_stock,raw_material_stock_history

admin.site.register(raw_material_list)
admin.site.register(raw_material_stock)
admin.site.register(raw_material_stock_history)