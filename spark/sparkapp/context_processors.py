# attendance/context_processors.py

from django.contrib.auth.models import Group

def is_teacher(request):
    """Check if the current user belongs to the 'HoD' group."""
    return {'is_teacher': request.user.groups.filter(name='Teacher').exists()}

def is_admin(request):
    """Check if the current user belongs to the 'HoD' group."""
    return {'is_admin': request.user.groups.filter(name='Admin').exists()}

def is_principal(request):
    """Check if the current user belongs to the 'HoD' group."""
    return {'is_principal': request.user.groups.filter(name='Principal').exists()}