from django.db import models

# Create your models here.
class Complain(models.Model):
	department=models.CharField(max_length=100)
	complain=models.TextField()
	add_time=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.department

class Suggestion(models.Model):
	department=models.CharField(max_length=100)
	suggestion=models.TextField()
	add_time=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.department

	

