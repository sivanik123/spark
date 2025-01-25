from django.urls import path
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # Login page
    path('register/', views.register, name='register'),  # Add this line for registration
    path('add-emp/', views.add_emp, name='add_emp'),  # Add data to the database
    path('add-department/', views.add_department, name='add_department'),
    path('add-designation/', views.add_designation, name='add_designation'),
    path('add-event-type/', views.add_event_type, name='add_event_type'),
    path('add-venue/', views.add_venue, name='add_venue'),  # Add a new venue
    path('add-role/', views.add_role, name='add_role'),  # Add role page
    path('add-role-assignment/', views.add_role_assignment, name='add_role_assignment'),  # Add role assignment page
    path('add-event/', views.add_event, name='add_event'),
    path('add-event-participation/', views.add_event_participation, name='add_event_participation'),
    path('logout/', views.logout_view, name='logout'),
    path('logout-success/', views.logout_success, name='logout_success'),
]
