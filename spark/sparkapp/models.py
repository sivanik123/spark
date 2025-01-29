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
    type_id = models.AutoField(primary_key=True)
    type_description = models.CharField(
        max_length=100,  # Adjust the max length as needed
        blank=False,  # Ensure it's not empty
    )

    def __str__(self):
        return self.type_description


class Venue(models.Model):
    venue_id = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    name = models.CharField(max_length=200)  # Venue name
    address = models.TextField()  # Venue address

    def __str__(self):
        return f"{self.name} - {self.address}"
    
class Role(models.Model):
    role_id = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    role_name = models.CharField(max_length=100)  # Name of the role
    role_description = models.TextField()  # Description of the role

    def __str__(self):
        return self.role_name  
    
class EmployeeRoleAssignment(models.Model):
    emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE)  # Reference Employee
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)  # Reference Role
    assigned_date = models.DateField()
    relieved_date = models.DateField(null=True, blank=True)
    document = models.FileField(upload_to="role_documents/", null=True, blank=True)

    def __str__(self):
        return f"{self.emp_id.emp_name} - {self.role_id.role_name}"
    
# Event model
class Event(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)  # Event title
    type_id = models.ForeignKey(EventType, on_delete=models.CASCADE)  # Reference to EventType
    from_date = models.DateField()  # Event start date
    to_date = models.DateField()  # Event end date
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)  # Reference to Venue

    def __str__(self):
        return self.title
    
# Event Participation model
class EventParticipation(models.Model):
    emp_id = models.ForeignKey('Employee', on_delete=models.CASCADE)  # String reference to Employee
    event_id = models.ForeignKey('Event', on_delete=models.CASCADE)  # String reference to Event
    doc_link = models.FileField(upload_to='participation_docs/', null=True, blank=True)  # File upload for proof

    def __str__(self):
        return f"{self.emp_id.emp_name} - {self.event_id.title}"