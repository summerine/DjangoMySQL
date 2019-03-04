from django.db import models

# Create your models here.
class Employee(models.Model):
	employee_id = models.CharField(max_length=20)
	employee_name = models.CharField(max_length=100)
	email = models.EmailField()
	employee_contact = models.CharField(max_length=15)
	class Meta:
		db_table = "employee"

		