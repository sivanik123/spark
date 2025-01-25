
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserForm, EmployeeForm,DepartmentForm,DesignationForm,EventTypeForm,VenueForm,RegisterForm,RoleForm,EmployeeRoleAssignmentForm,EventForm,EventParticipationForm
from django.contrib.auth.models import User
from django.contrib.auth import logout
#from .models import Department, Designation


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

@login_required
def add_venue(request):
    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new venue
            return redirect('index')  # Redirect to the home page (you can modify this as needed)
    else:
        form = VenueForm()
    return render(request, 'add_venue.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            messages.success(request, 'Registration successful!')
            return redirect('index')  # Redirect to home page after successful registration
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})@login_required
def add_role(request):
    if request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new role
            return redirect('index')  # Redirect to the home page
    else:
        form = RoleForm()
    return render(request, 'add_role.html', {'form': form})


@login_required
def add_role(request):
    if request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new role
            return redirect('index')  # Redirect to the home page
    else:
        form = RoleForm()
    return render(request, 'add_role.html', {'form': form})

@login_required
def add_role_assignment(request):
    if request.method == 'POST':
        form = EmployeeRoleAssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the new assignment
            return redirect('index')  # Redirect to the home page
    else:
        form = EmployeeRoleAssignmentForm()
    return render(request, 'add_role_assignment.html', {'form': form})


@login_required
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Event added successfully!")
            return redirect('index')
    else:
        form = EventForm()
    return render(request, 'add_event.html', {'form': form})

@login_required
def add_event_participation(request):
    if request.method == 'POST':
        form = EventParticipationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Event Participation added successfully!")
            return redirect('index')
    else:
        form = EventParticipationForm()
    return render(request, 'add_event_participation.html', {'form': form})

def logout_view(request):
    logout(request)  # Logs out the user
    return redirect('logout_success')  # Redirects to a thank you page or home page
def logout_success(request):
    return render(request, 'logout_success.html')
