from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.permissions import BasePermission

class IsStaffOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

class IsOwnerOrStaff(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.user == request.user