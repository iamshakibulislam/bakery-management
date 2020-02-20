from django.db import models
import datetime

today=datetime.date.today().strftime("%Y-%m-%d")



class employee_list(models.Model):
	name=models.CharField(max_length=25,unique=True)
	salary=models.FloatField(max_length=7)

class attendence(models.Model):
	date=models.DateField(auto_now_add=False,auto_now=False,default=today)
	name=models.ForeignKey(employee_list,on_delete=models.SET_NULL,null=True)
	status=models.BooleanField()
	add_salary=models.FloatField()


class pay_employee(models.Model):
	date=models.DateField(auto_now=False,auto_now_add=False,default=today)
	name=models.ForeignKey(employee_list,on_delete=models.CASCADE)
	amount=models.FloatField(max_length=10)
