# api/permissions.py
from rest_framework.permissions import BasePermission

class IsSpecialUser(BasePermission):
    """
    Allow access only if user has attribute is_special == True
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and getattr(request.user, 'is_special', False))
