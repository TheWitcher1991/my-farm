from dataclasses import dataclass
from typing import NewType, TypedDict

from django.db import models

from packages.kernel.utils import t

UserId = NewType("UserId", int)


class UserRole(models.TextChoices):
    SUPERADMIN = "superadmin", t("Супер-администратор")
    ADMIN = "admin", t("Администратор")
    USER = "user", t("Оператор")


@dataclass(frozen=True)
class CreateUserDTO:
    pass


class CreateUserData(TypedDict):
    pass
