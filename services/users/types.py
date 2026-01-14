from typing import NewType

from django.db import models

from packages.kernel.utils import t

UserId = NewType("UserId", int)


class UserRole(models.TextChoices):
    SUPERADMIN = "superadmin", t("Супер-администратор")
    ADMIN = "admin", t("Администратор")
    USER = "operator", t("Оператор")
