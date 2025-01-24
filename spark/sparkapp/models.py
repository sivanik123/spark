from django.db import models
from django.contrib.auth.models import User

# Department model
class Department(models.Model):
    dept_id = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    dept_name = models.CharField(max_length=100)  # Department name

    def _str_(self):  # Corrected method name
        return f"{self.dept_name}"

# Designation model
class Designation(models.Model):
    designation_id = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    designation_name = models.CharField(max_length=100)  # Designation name (e.g., "Manager", "Developer")

    def _str_(self):  # Corrected method name
        return f'{self.designation_name}'

# Employee model
class Employee(models.Model):   
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    emp_name = models.CharField(max_length=200)  # Employee's full name
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)  # Profile picture
    email_id = models.EmailField(unique=True)  # Unique email
    phn_no = models.CharField(max_length=15)  # Phone number
    adhar_no = models.CharField(max_length=12, unique=True)  # Aadhaar number
    dept_id = models.ForeignKey(Department, on_delete=models.CASCADE)  # Foreign key reference to Department
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])  # Gender with choices
    DOB = models.DateField()  # Date of birth
    date_of_joining = models.DateField()  # Date the employee joined
    current_address = models.TextField()  # Current address
    residential_address = models.TextField()  # Residential address
    status = models.CharField(max_length=50, choices=[('Active', 'Active'), ('Inactive', 'Inactive')])  # Employment status with choices
    designation_id = models.ForeignKey(Designation, on_delete=models.CASCADE)  # Foreign key reference to Designation

    def _str_(self):  # Corrected method name
        return f'{self.emp_name} ({self.designation_id.designation_name})'
    from django.db import models

class EventType(models.Model):
    type_id = models.AutoField(primary_key=True)  # Auto-incremented primary key
    type_description = models.CharField(max_length=200)  # Description of the event type

    def __str__(self):
        return self.type_description
