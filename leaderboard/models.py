from django.db import models
from datetime import datetime
# Create your models here.

class point_table(models.Model):
	user_id=models.CharField(max_length=20)
	challenge_code=models.CharField(max_length=10)
	maxscore=models.IntegerField(default=0)
	time= models.DateTimeField(auto_now=True, blank=True)

class problem_score(models.Model):
	challenge_code=models.CharField(max_length=20)
	user_id=models.CharField(max_length=20)
	problem_code=models.CharField(max_length=10)
	score=models.IntegerField(default=0)
	time=models.DateTimeField(auto_now=True, blank=True)
