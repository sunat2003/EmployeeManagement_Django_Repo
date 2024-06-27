from django.db import models

class Employee(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    dept=models.CharField(max_length=100)
    salary=models.IntegerField()
    bonus=models.IntegerField()
    role=models.CharField(max_length=100)
    phone=models.IntegerField()

    