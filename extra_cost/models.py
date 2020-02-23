from django.db import models
import datetime
today=datetime.date.today().strftime("%Y-%m-%d")
# Create your models here.

class extra_cost(models.Model):
	date=models.DateField(auto_now_add=False,auto_now=False,default=today)
	name=models.CharField(max_length=30)
	cost=models.FloatField(max_length=30)

	def __str__(self):
		return self.name