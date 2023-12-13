from django.contrib import admin
from .models import Department, Course, Person
# Register your models here.

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Department, DepartmentAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'department']
admin.site.register(Course, CourseAdmin)

