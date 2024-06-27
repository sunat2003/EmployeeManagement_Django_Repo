import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','EmployeeManagementProject.settings')
import django
django.setup()

from faker import Faker
from  random import *
from testapp.models import Employee
fake=Faker()


def fakemobile_num():
    d1=randint(6,9)
    no=''+str(d1)
    for i in range(9):
        no+=str(randint(0,9))
    return int(no)

def fakedatails(n):
    for i in range(n):
        department=['Developer','Testing','Training','AI','Mechine Learning','Deap Learning','Deployer']
        role=['HR','Manager','Developer','Team Lead','Junier Developer','Senier Developer']
        fs_firstname=fake.first_name()
        fs_lastname=fake.last_name()
        fs_dept=choice(department)
        fs_salary=fake.random_int(min=1,max=999999)
        fs_bonus=fake.random_int(min=1,max=9999)
        fs_role=choice(role)
        fs_mobile=fakemobile_num()
        Employee.objects.get_or_create(first_name=fs_firstname,last_name=fs_lastname,dept=fs_dept, salary=fs_salary,bonus=fs_bonus,role=fs_role,phone=fs_mobile)
n=int(input("Enter the number of Employeet"))
fakedatails(n)
print("Details are updates succsesfully")
