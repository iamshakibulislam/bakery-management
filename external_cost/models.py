from django.db import models

import datetime
#raw_materials model register here
today=datetime.date.today().strftime("%Y-%m-%d")

class external_cost_list(models.Model):
	item=models.CharField(max_length=40,unique=True)
	price=models.FloatField(max_length=12)

	def __str__(self):
		return self.item



class external_cost_stock(models.Model):
	item=models.ForeignKey(external_cost_list,on_delete=models.CASCADE)
	quantity=models.FloatField(max_length=12)
	value=models.FloatField(max_length=12)

	def __str__(self):
		return self.item.item


class external_cost_stock_history(models.Model):

	date=models.DateField(auto_now_add=False,auto_now=False,default=today)
	item=models.ForeignKey(external_cost_list,on_delete=models.CASCADE)
	quantity=models.FloatField()


	def __str__(self):
		return self.item.item

class external_cost_expense(models.Model):
	date=models.DateField(auto_now_add=False,auto_now=False,default=today)
	item=models.ForeignKey(external_cost_list,on_delete=models.CASCADE)
	quantity=models.FloatField(max_length=20)
	value=models.FloatField(max_length=20,null=True)
