from rest_framework import permissions

class IsAdminUserRole(permissions.BasePermission):
    """
    Custom permission to allow only users with role 'admin' to modify data.
    """

    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.is_authenticated
            and getattr(request.user, 'role', '') == 'admin'
        )

