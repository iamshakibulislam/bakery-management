from django.db import models
import datetime
from raw_materials.models import raw_material_list
today=datetime.date.today().strftime("%Y-%m-%d")

class product_list(models.Model):
	name=models.CharField(max_length=40,null=False,unique=True)
	price=models.IntegerField()
	raw_materials=models.ManyToManyField(raw_material_list,through='product_rawmaterial')


	def __str__(self):
		return self.name

class product_rawmaterial(models.Model):
	quantity=models.FloatField(max_length=20)
	material=models.ForeignKey(raw_material_list,on_delete=models.CASCADE)
	product=models.ForeignKey(product_list,on_delete=models.CASCADE)
	



class product_stock(models.Model):
	name=models.ForeignKey(product_list,on_delete=models.CASCADE)
	quantity=models.IntegerField()
	value=models.FloatField(max_length=20)


class product_stock_history(models.Model):
	date=models.DateField(auto_now=False,auto_now_add=False,default=today)
	name=models.ForeignKey(product_list,on_delete=models.CASCADE)
	quantity=models.IntegerField()
	raw_mat_value=models.FloatField(max_length=30,null=False,default=0)


