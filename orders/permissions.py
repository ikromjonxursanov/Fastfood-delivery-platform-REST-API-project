from rest_framework.permissions import BasePermission

class IsAuthenticatedOrReadOnlyForOrder(BasePermission):
    def has_permission(self, request, user):
        if request.method == "PROFILE":
            return request.user.is_authenticated
        return True


