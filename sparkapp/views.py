from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import UserForm, EmployeeForm, DepartmentForm, DesignationForm, EventTypeForm, VenueForm, RegisterForm, RoleForm, EmployeeRoleAssignmentForm, EventForm, EventParticipationForm
from .models import Department, Designation, EventType, Role, EmployeeRoleAssignment, Event, EventParticipation
from django.contrib.auth.forms import AuthenticationForm

def admin_group_required(user):
    return user.groups.filter(name='Admin').exists()


def teacher_group_required(user):
    return user.groups.filter(name='Teacher').exists()


def principal_group_required(user):
    return user.groups.filter(name='Principal').exists()

# Home page
@login_required
def index(request):
    return render(request, 'index.html')


# Add Employee
@login_required
def add_emp(request):
    if request.user.groups.filter(name='Teacher').exists():
        full_form = True  # Teacher gets the full form
    elif request.user.groups.filter(name='Admin').exists():
        full_form = False  # Admin gets a limited form
    else:
        return redirect('access_denied')  # Restrict other users

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        employee_form = EmployeeForm(request.POST, request.FILES) if full_form else EmployeeForm(request.POST)

        if user_form.is_valid() and employee_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])  # Set hashed password
            user.save()

            employee = employee_form.save(commit=False)
            employee.user = user
            employee.save()

            messages.success(request, 'Employee added successfully!')
            return redirect('index')
    else:
        user_form = UserForm()
        employee_form = EmployeeForm()

    return render(request, 'add_emp.html', {
        'user_form': user_form,
        'employee_form': employee_form,
        'full_form': full_form,
    })


# Department Views
@login_required
@user_passes_test(admin_group_required)
def add_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new department
            return redirect('index')
    else:
        form = DepartmentForm()
    return render(request, 'add_dept.html', {'form': form})


# Designation Views
@login_required
@user_passes_test(admin_group_required)
def manage_designation(request):
    designations = Designation.objects.all()
    return render(request, 'manage_designation.html', {'designations': designations})


# Add Designation
@login_required
@user_passes_test(admin_group_required)
def add_designation(request):
    if request.method == 'POST':
        form = DesignationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_designation')
    else:
        form = DesignationForm()
    return render(request, 'add_designation.html', {'form': form})


# Edit Designation
@login_required
@user_passes_test(admin_group_required)
def edit_designation(request, designation_id):
    designation = get_object_or_404(Designation, pk=designation_id)
    if request.method == 'POST':
        form = DesignationForm(request.POST, instance=designation)
        if form.is_valid():
            form.save()
            return redirect('manage_designation')
    else:
        form = DesignationForm(instance=designation)
    return render(request, 'edit_designation.html', {'form': form})


# Delete Designation
@login_required
@user_passes_test(admin_group_required)
def delete_designation(request, designation_id):
    designation = get_object_or_404(Designation, pk=designation_id)
    designation.delete()
    return redirect('manage_designation')


# Event Type Views
@login_required
@user_passes_test(admin_group_required)
def manage_event_type(request):
    event_types = EventType.objects.all()
    return render(request, 'manage_event_type.html', {'event_types': event_types})


# Add Event Type
@login_required
@user_passes_test(admin_group_required)
def add_event_type(request):
    if request.method == 'POST':
        form = EventTypeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Event Type added successfully.")
            return redirect('manage_event_type')
    else:
        form = EventTypeForm()

    return render(request, 'add_event_type.html', {'form': form})


# Edit Event Type
@login_required
@user_passes_test(admin_group_required)
def edit_event_type(request, type_id):
    event_type = get_object_or_404(EventType, type_id=type_id)
    
    # Initialize the form with the existing instance
    form = EventTypeForm(instance=event_type)

    if request.method == 'POST':
        form = EventTypeForm(request.POST, instance=event_type)
        if form.is_valid():
            form.save()
            messages.success(request, "Event Type updated successfully.")
            return redirect('manage_event_type')

    return render(request, 'edit_event_type.html', {'form': form, 'event_type': event_type})

# Delete Event Type
@login_required
@user_passes_test(admin_group_required)
def delete_event_type(request, type_id):
    event_type = get_object_or_404(EventType, type_id=type_id)
    event_type.delete()
    return redirect('manage_event_type')


# Venue Views
@login_required
@user_passes_test(admin_group_required)
def add_venue(request):
    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = VenueForm()
    return render(request, 'add_venue.html', {'form': form})


# Registration
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            password = form.cleaned_data['password']  # Get password from the form
            user.set_password(password)  # Hash and set the password
            user.save()  # Save the user with the password
            login(request, user)
            messages.success(request, 'Registration successful!')

            # Redirect based on user role
            if user.is_superuser:
                return redirect('admin_dashboard')
            elif user.groups.filter(name='Teachers').exists():
                return redirect('teacher_dashboard')
            elif user.groups.filter(name='Principals').exists():
                return redirect('principal_dashboard')
            else:
                return redirect('index')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


# Role Views
@login_required
@user_passes_test(admin_group_required)
def add_role(request):
    if request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new role
            return redirect('index')
    else:
        form = RoleForm()
    return render(request, 'add_role.html', {'form': form})


# Employee Role Assignment Views
@login_required
@user_passes_test(teacher_group_required)
def add_role_assignment(request):
    if request.method == 'POST':
        form = EmployeeRoleAssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the new assignment
            return redirect('index')
    else:
        form = EmployeeRoleAssignmentForm()
    return render(request, 'add_role_assignment.html', {'form': form})


# Event Views
@login_required
@user_passes_test(admin_group_required)
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


# Event Participation Views
@login_required
@user_passes_test(teacher_group_required)
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


# Logout Views
def logout_view(request):
    logout(request)
    return redirect('logout_success')


def logout_success(request):
    return render(request, 'logout_success.html')


# Admin Dashboard View
@login_required
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')


# Teacher Dashboard View
@login_required
def teacher_dashboard(request):
    return render(request, 'teacher_dashboard.html')


# Principal Dashboard View
@login_required
def principal_dashboard(request):
    return render(request, 'principal_dashboard.html')


# Access Denied View
@login_required
def access_denied(request):
    return render(request, 'access_denied.html')
# Manage Departments
@login_required
@user_passes_test(admin_group_required)
def manage_department(request):
    departments = Department.objects.all()
    return render(request, 'departments/manage_department.html', {'departments': departments})

# Add Department
@login_required
@user_passes_test(admin_group_required)
def add_department(request):
    form = DepartmentForm()
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_department')  # Redirect to department management page

    departments = Department.objects.all()  # Fetch all departments
    return render(request, 'departments/add_department.html', {'form': form, 'departments': departments})

# Edit Department
@login_required
@user_passes_test(admin_group_required)
def edit_department(request, dept_id):
    department = get_object_or_404(Department, dept_id=dept_id)
    
    if request.method == "POST":
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('manage_department')  # Redirect to manage_department
    
    else:
        form = DepartmentForm(instance=department)

    return render(request, 'departments/edit_department.html', {'form': form})

# Delete Department
@login_required
@user_passes_test(admin_group_required)
def delete_department(request, dept_id):
    department = get_object_or_404(Department, dept_id=dept_id)
    department.delete()
    return redirect('manage_department')  # Redirect to manage_department
@login_required
@user_passes_test(principal_group_required)
def principal_dashboard(request):
    teachers = User.objects.filter(groups__name='Teacher').select_related('employee')

    return render(request, 'principal_dashboard.html', {
        'teachers': teachers,
    })

from django.shortcuts import render, get_object_or_404
from .models import Employee

@login_required
@user_passes_test(principal_group_required)
def teacher_details(request, user_id):
    # Fetch the Employee using the User ID
    try:
        employee = Employee.objects.get(user__id=user_id)  # user__id is used to filter the related User
    except Employee.DoesNotExist:
        # If the Employee doesn't exist, handle the error, maybe show a 404 page
        return render(request, '404.html', {'message': 'Employee not found!'})

    # Now get the events the employee participated in (if any)
    events = Event.objects.filter(eventparticipation__emp_id=employee)
    
    # Pass the employee data to the template
    return render(request, 'teacher_details.html', {
        'employee': employee,
        'events': events
    })  

from django.http import Http404

@login_required
@user_passes_test(principal_group_required)
def teacher_details(request, user_id):
    try:
        employee = Employee.objects.get(user__id=user_id)
    except Employee.DoesNotExist:
        raise Http404("Employee not found")

    events = Event.objects.filter(eventparticipation__emp_id=employee)

    return render(request, 'teacher_details.html', {
        'employee': employee,
        'events': events
    })
