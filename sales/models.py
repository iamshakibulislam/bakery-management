from django.db import models
import datetime
from production.models import product_list
# Create your models here.
today=datetime.date.today().strftime("%Y-%m-%d")

class saleman_list(models.Model):
	name=models.CharField(max_length=15)
	commission=models.FloatField(max_length=5)
	mobile=models.CharField(max_length=15)
	product=models.ManyToManyField(product_list,through='saleman_sale')


	def __str__(self):
		return self.name


class saleman_sale(models.Model):
	date=models.DateField(auto_now_add=False,auto_now=False,default=today)
	name=models.ForeignKey(saleman_list,on_delete=models.CASCADE)
	product=models.ForeignKey(product_list,on_delete=models.SET_NULL,null=True)
	quantity=models.IntegerField()
	value=models.FloatField(max_length=20)
	after_commission_value=models.FloatField(max_length=20)



class retail_sales(models.Model):
	
	date=models.DateField(auto_now=False,auto_now_add=False,default=today)
	name=models.CharField(max_length=15)
	product=models.ManyToManyField(product_list,through='retail')

	def __str__(self):
		return self.name



class retail(models.Model):
	date=models.DateField(auto_now=False,auto_now_add=False,default=today)
	name=models.ForeignKey(retail_sales,on_delete=models.CASCADE)
	quantity=models.IntegerField()
	product=models.ForeignKey(product_list,on_delete=models.CASCADE)
	value=models.FloatField(max_length=20)

	def __str__(self):
		return self.name


class deposit_from_saleman(models.Model):
	date=models.DateField(auto_now_add=False,auto_now=False,default=today)
	name=models.ForeignKey(saleman_list,on_delete=models.CASCADE)
	amount=models.IntegerField()

	def __str__(self):
		return self.name


class pay_retail(models.Model):
	date=models.DateField(auto_now=False,auto_now_add=False,default=today)
	name=models.ForeignKey(retail_sales,on_delete=models.CASCADE)
	amount=models.IntegerField()

	def __str__(self):
		return self.name


