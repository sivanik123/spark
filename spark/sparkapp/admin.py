from django.contrib import admin
from .models import Department, Designation, Employee

# Customizing the Department admin
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('dept_id', 'dept_name')  # Display fields in the admin list view
    search_fields = ('dept_name',)  # Add search functionality for department names
    ordering = ('dept_name',)  # Default ordering by department name

# Customizing the Designation admin
@admin.register(Designation)
class DesignationAdmin(admin.ModelAdmin):
    list_display = ('designation_id', 'designation_name')  # Display fields in the admin list view
    search_fields = ('designation_name',)  # Add search functionality for designation names
    ordering = ('designation_name',)  # Default ordering by designation name

# Customizing the Employee admin
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('emp_name', 'email_id', 'phn_no', 'adhar_no', 'dept_id', 'designation_id', 'status')  # Fields to display in the admin list view
    list_filter = ('dept_id', 'designation_id', 'status')  # Add filters for department, designation, and status
    search_fields = ('emp_name', 'email_id', 'adhar_no')  # Add search functionality for name, email, and Aadhaar
    ordering = ('emp_name',)  # Default ordering by employee name
    fieldsets = (
        ('Personal Information', {
            'fields': ('emp_name', 'profile_pic', 'email_id', 'phn_no', 'adhar_no', 'gender', 'DOB')
        }),
        ('Job Details', {
            'fields': ('dept_id', 'designation_id', 'date_of_joining', 'status')
        }),
        ('Address Information', {
            'fields': ('current_address', 'residential_address')
        }),
    )  # Organize fields into logical groups


