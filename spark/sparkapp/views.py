
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserForm, EmployeeForm,DepartmentForm,DesignationForm,EventTypeForm
from django.contrib.auth.models import User
from .models import Department, Designation


# Home page
@login_required
def index(request):
    return render(request, 'index.html')

# Add data to the table
@login_required
def add_emp(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        employee_form = EmployeeForm(request.POST, request.FILES)
        if user_form.is_valid() and employee_form.is_valid():
            # Save User
            user = user_form.save()
            # Save Employee with User instance
            employee = employee_form.save(commit=False)
            employee.user = user
            employee.save()
            return redirect('index')  # Redirect to a success page
    else:
        user_form = UserForm()
        employee_form = EmployeeForm()
    return render(request, 'add_emp.html', {'user_form': user_form, 'employee_form': employee_form})
# View to add a new Department
@login_required
def add_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new department
            return redirect('index')  # Redirect to a department list page (you can modify this)
    else:
        form = DepartmentForm()
    return render(request, 'add_dept.html', {'form': form})

# View to add a new Designation
@login_required
def add_designation(request):
    if request.method == 'POST':
        form = DesignationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new designation
            return redirect('index')  # Redirect to a designation list page (you can modify this)
    else:
        form = DesignationForm()
    return render(request, 'add_designation.html', {'form': form})

@login_required
def add_event_type(request):
    if request.method == 'POST':
        form = EventTypeForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new event type
            messages.success(request, "Event Type added successfully.")
            return redirect('index')  # Redirect to the homepage or another success page
    else:
        form = EventTypeForm()
    
    return render(request, 'add_event_type.html', {'form': form})