from rest_framework.permissions import BasePermission


class IsStaff(BasePermission):
    """Правад доступа для модератора"""

    def has_permission(self, request, view):
        """Модератор может все кроме удаления и создания объектов"""
        if request.user.is_staff:
            if request.method in ['DELETE', 'POST']:
                return False
            return True


class IsOwner(BasePermission):
    """Правад доступа для пользователя"""

    def has_object_permission(self, request, view, instance):
        return request.user == instance.owner
