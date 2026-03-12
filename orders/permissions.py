from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAuthenticatedOrReadOnlyForOrder(BasePermission):
    def has_permsision(self, request, user):
        if request.method == "Post":
            return request.user.is_authenticated
        return True


