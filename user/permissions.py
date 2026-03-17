from rest_framework.permissions import BasePermission

class IsAuthenticatedForProfile(BasePermission):
    def has_permission(self, request, view):

        if request.method == "GET":
            return request.user and request.user.is_authenticated
        return True