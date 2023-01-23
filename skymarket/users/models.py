from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db.models import CharField, EmailField, TextChoices, ImageField, BooleanField
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class UserRoles(TextChoices):
    """
    Описывает роли пользователя
    """
    USER = "user", _("user")
    ADMIN = "admin", _("admin")


class User(AbstractBaseUser):
    """
    Описывает пользователя
    """
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email

    # эта константа определяет поле для логина пользователя
    USERNAME_FIELD = 'email'

    # эта константа содержит список с полями,
    # которые необходимо заполнить при создании суперпользователя
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role"]

    # Сообщает Django, что класс UserManager
    # должен управлять объектами этого типа.
    objects = UserManager()

    first_name = CharField(db_index=True, max_length=200)
    last_name = CharField(db_index=True, max_length=200)
    email = EmailField(db_index=True, unique=True)
    phone = PhoneNumberField(max_length=12)
    role = CharField(max_length=5, choices=UserRoles.choices)
    image = ImageField(null=True, blank=True, upload_to="django_media")
    is_active = BooleanField(default=True)

    @property
    def is_admin(self):
        """
        Проверяет статус администратора
        """
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        """
        Проверяет статус простого пользователя
        """
        return self.role == UserRoles.USER

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin
