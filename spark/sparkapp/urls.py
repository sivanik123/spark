from django.urls import path
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # Login page
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),  # Logout
    path('add-emp/', views.add_emp, name='add_emp'),  # Add data to the database
    path('add-department/', views.add_department, name='add_department'),
    path('add-designation/', views.add_designation, name='add_designation'),
]
