from django.db import models

class problem_details(models.Model):
	challenge_code=models.CharField(max_length=10)
	problem_name=models.CharField(max_length=10)
	problem_code=models.CharField(max_length=10,primary_key=True)
	difficulty=models.CharField(max_length=10)
	
class compete_details(models.Model):
	challenge_name=models.CharField(max_length=50)
	challenge_code=models.CharField(max_length=10,primary_key=True)
	challenge_status=models.CharField(max_length=10)
	start_time=models.DateTimeField(blank=True)
	end_time=models.DateTimeField(blank=True)
	
	