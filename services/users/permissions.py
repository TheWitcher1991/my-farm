from rest_framework.permissions import SAFE_METHODS, BasePermission

from packages.kernel.types import ExtendedRequest
from users.types import UserRole


class IsAuthenticated(BasePermission):

    def has_permission(self, request: ExtendedRequest, view):
        return bool(request.user and request.user.is_authenticated)


class IsSuperUser(IsAuthenticated):

    def has_permission(self, request: ExtendedRequest, view):
        return bool(request.user.is_superuser)


class IsUser(IsAuthenticated):

    def has_permission(self, request: ExtendedRequest, view):
        return bool(request.user.role == UserRole.USER)


class IsAdminOrReadOnly(BasePermission):

    def has_permission(self, request: ExtendedRequest, view):
        if not request.user or not request.user.is_authenticated:
            return False

        if request.method in SAFE_METHODS and request.user.role == UserRole.USER:
            return True

        if request.method not in SAFE_METHODS and request.user.role == UserRole.USER:
            return False

        if request.user.role == UserRole.ADMIN:
            return True

        return False
