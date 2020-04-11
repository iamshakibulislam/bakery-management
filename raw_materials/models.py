from django.db import models
import datetime
#raw_materials model register here
today=datetime.date.today().strftime("%Y-%m-%d")

class raw_material_list(models.Model):
	item=models.CharField(max_length=40,unique=True)
	price=models.FloatField(max_length=12)

	def __str__(self):
		return self.item



class raw_material_stock(models.Model):
	item=models.ForeignKey(raw_material_list,on_delete=models.CASCADE)
	quantity=models.FloatField()
	value=models.FloatField(max_length=12)

	def __str__(self):
		return self.item.item


class raw_material_stock_history(models.Model):

	date=models.DateField(auto_now_add=False,auto_now=False,default=today)
	item=models.ForeignKey(raw_material_list,on_delete=models.CASCADE)
	quantity=models.FloatField()


	def __str__(self):
		return self.item.item
