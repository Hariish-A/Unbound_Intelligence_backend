from rest_framework import permissions


class AdminOnlyEditPermission(permissions.BasePermission):
    """
    Allow GET and LIST for all, but restrict Create, Update, and Delete to superusers.
    """

    def has_permission(self, request, view):
        # Allow any user for safe methods (GET, LIST)
        if request.method in permissions.SAFE_METHODS:
            return True

        # Only allow superusers for Create, Update, Delete
        return request.user and request.user.is_superuser