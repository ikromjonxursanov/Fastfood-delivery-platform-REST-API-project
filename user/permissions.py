from rest_framework.permissions import BasePermission

class IsAuthenticatedOrReadOnlyForOrder(BasePermission):
    def has_permission(self, request, view):

        if request.method == "POST":
            return request.user.is_authenticated
        return True