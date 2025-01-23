from django import forms
from django.contrib.auth.models import User
from .models import Employee, Department, Designation
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