from rest_framework.permissions import BasePermission


class IsAnonymous(BasePermission):
    """
    Allows access only to anonymous users.
    """

    def has_permission(self, request, view):
        return bool(request.user and not request.user.is_authenticated)
