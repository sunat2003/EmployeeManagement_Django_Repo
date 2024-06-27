from django.shortcuts import render,redirect
from testapp.models import Employee
from django.http import HttpResponse
from django.db.models import Q
from testapp.forms import EmployeeForm
#home view
def home_view(request):
    return render(request,'testapp/home.html')

#all the employee view(R)
def view_Employee_view(request):
    emp=Employee.objects.all()
    return render(request,'testapp/view.html',{"emp":emp})

#add employee
def add_Emplyee_view(request):
    if request.method=='POST':
        try:
            firstname=request.POST['firstname']
            lastname=request.POST['lastname']
            dept=request.POST['dept']
            salary=request.POST['salary']
            bonus=request.POST['bonus']
            role=request.POST['role']
            phone=request.POST['phone']
            emp=Employee(first_name=firstname,last_name=lastname,dept=dept,salary=salary,bonus=bonus,role=role,phone=phone)
            emp.save()
            return redirect('home')
        except ValueError:
            return redirect('add_Emplyee_view')
    elif request.method=='GET':
        return render(request,'testapp/add.html')
    else:
        return HttpResponse("You entered worong details")


#remove data
def remove_Employee_view(request,id=0):
    if id:
        try:
            emp=Employee.objects.get(id=id)
            emp.delete()
            return HttpResponse('Employee deleted Succesfully')
        except:
            return HttpResponse("Enter the valid id ")
    emp=Employee.objects.all()
    return render(request,'testapp/remove.html',{"emp":emp})


#filter employee
def filter_Employee_view(request):
    if request.method=='POST':
        try:
            name=request.POST['name']
            role=request.POST['role']
            dept=request.POST['dept']
            emp=Employee.objects.all()
            if name:
                 emps=emp.filter( Q(first_name__icontains=name) | Q(last_name__icontains=name))
            if role:
                 emps=emp.filter(role=role)
            if dept:
                 emps=emp.filter(dept=dept)
            return render(request,'testapp/view.html',{"emp":emps})
        except UnboundLocalError:
            return redirect('filter_Employee_view')
    return render(request,'testapp/filter.html')

def update_view(request,id=0):
    if id:
        emp=Employee.objects.get(id=id)
        form=EmployeeForm(instance=emp)
        if request.method=="POST":
            form=EmployeeForm(request.POST,instance=emp)
            if form.is_valid():
                form.save()
                return redirect('update_view')
        return render(request,'testapp/updateform.html',{"form":form})
    emp_data=Employee.objects.all()
    return render(request,'testapp/update.html',{"emp_data":emp_data})