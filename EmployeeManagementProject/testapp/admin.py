from django.contrib import admin
from testapp.models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','dept','salary','bonus','role','phone']
admin.site.register(Employee,EmployeeAdmin)