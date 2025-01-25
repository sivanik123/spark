from django import forms
from django.contrib.auth.models import User
from .models import Employee, Department, Designation,EventType,Venue,Role,EmployeeRoleAssignment, Event,EventParticipation
from django.contrib.auth.forms import UserCreationForm

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['dept_name']
        widgets = {
            'dept_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Department Name'}),
        }

class DesignationForm(forms.ModelForm):
    class Meta:
        model = Designation
        fields = ['designation_name']
        widgets = {
            'designation_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Designation Name'}),
        }

class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Ensure email is a required field

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'emp_name',
            'profile_pic',
            'email_id',
            'phn_no',
            'adhar_no',
            'dept_id',
            'gender',
            'DOB',
            'date_of_joining',
            'current_address',
            'residential_address',
            'status',
            'designation_id',
        ]
        widgets = {
            'DOB': forms.DateInput(attrs={'type': 'date'}),
            'date_of_joining': forms.DateInput(attrs={'type': 'date'}),
            'current_address': forms.Textarea(attrs={'rows': 3}),
            'residential_address': forms.Textarea(attrs={'rows': 3}),
        }

class UserEmployeeForm(forms.ModelForm):
    username = forms.CharField(label="Username", max_length=150)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    email = forms.EmailField(label="Email")
    
    class Meta:
        model = Employee
        fields = [
            'emp_name',
            'profile_pic',
            'phn_no',
            'adhar_no',
            'dept_id',
            'gender',
            'DOB',
            'date_of_joining',
            'current_address',
            'residential_address',
            'status',
            'designation_id',
        ]

class EventTypeForm(forms.ModelForm):
    class Meta:
        model = EventType
        fields = ['type_description']
        widgets = {
            'type_description': forms.Select(attrs={'class': 'form-control'}),
        }

class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ['name', 'address']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Venue Name'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Venue Address', 'rows': 3}),
        }

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['role_name', 'role_description']
        widgets = {
            'role_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Role Name'}),
            'role_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter Role Description'}),
        }

class EmployeeRoleAssignmentForm(forms.ModelForm):
    class Meta:
        model = EmployeeRoleAssignment
        fields = ['emp_id', 'role_id', 'assigned_date', 'relieved_date', 'document']
        widgets = {
            'assigned_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'relieved_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'type_id', 'from_date', 'to_date', 'venue']
        widgets = {
            'from_date': forms.DateInput(attrs={'type': 'date'}),
            'to_date': forms.DateInput(attrs={'type': 'date'}),
        }


class EventParticipationForm(forms.ModelForm):
    class Meta:
        model = EventParticipation
        fields = ['emp_id', 'event_id', 'doc_link']
        widgets = {
            'doc_link': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }