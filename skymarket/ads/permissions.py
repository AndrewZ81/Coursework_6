from rest_framework.permissions import BasePermission

from users.models import UserRoles


class AdRetrieveUpdateDestroyPermission(BasePermission):
    """
    Разграничивает права доступа авторизованных пользователей
    """
    message = "Доступ разрешён только администратору или владельцу записи"

    def has_object_permission(self, request, view, obj):
        if request.method == "GET":
            return True
        if request.user.role == UserRoles.ADMIN or request.user.id == obj.author_id:
            return True
        return False
