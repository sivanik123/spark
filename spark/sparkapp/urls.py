from django.urls import path
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # Login page
    path('register/', views.register, name='register'),  # Add this line for registration
    path('manage-emp/', views.add_emp, name='manage_emp'),  # Change add_emp to manage_emp
    path('manage-department/', views.add_department, name='manage_department'),
    path('manage-event-type/', views.add_event_type, name='manage_event_type'),
    path('manage-venue/', views.add_venue, name='manage_venue'),
    path('manage-role/', views.add_role, name='manage_role'),
    path('manage-role-assignment/', views.add_role_assignment, name='manage_role_assignment'),
    path('manage-event/', views.add_event, name='manage_event'),
    path('manage-event-participation/', views.add_event_participation, name='manage_event_participation'),
    path('logout/', views.logout_view, name='logout'),
    path('logout-success/', views.logout_success, name='logout_success'),
    path('edit-event-type/<int:type_id>/', views.edit_event_type, name='edit_event_type'),
    path('delete-event-type/<int:type_id>/', views.delete_event_type, name='delete_event_type'),
    path('manage-designation/', views.manage_designation, name='manage_designation'),
    path('add-designation/', views.add_designation, name='add_designation'),
    path('edit-designation/<int:designation_id>/', views.edit_designation, name='edit_designation'),
    path('delete-designation/<int:designation_id>/', views.delete_designation, name='delete_designation'),
]