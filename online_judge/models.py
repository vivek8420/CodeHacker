from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
class submissions(models.Model):
	sub_num=models.IntegerField(default=0,primary_key=True)
	user_id=models.CharField(max_length=50)
	problem_code=models.CharField(max_length=10)
	challnge_name=models.CharField(max_length=50)
	sub_status= models.BooleanField(default = True)
	time= models.DateTimeField(auto_now_add=True, blank=True)


