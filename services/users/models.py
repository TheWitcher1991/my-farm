from django.db import models

from config.settings import CHAR_MAX_LENGTH
from packages.kernel.adapters import UserModelAdapter
from packages.kernel.utils import t
from users.managers import UserManager
from users.types import UserRole


class User(UserModelAdapter):
    email = models.EmailField(t("Email"), max_length=CHAR_MAX_LENGTH, unique=True)
    phone = models.TextField(t("Телефон"), max_length=36, unique=True)
    password = models.CharField(t("Пароль"), max_length=CHAR_MAX_LENGTH)
    first_name = models.CharField(t("Имя"), max_length=CHAR_MAX_LENGTH)
    last_name = models.CharField(t("Фамилия"), max_length=CHAR_MAX_LENGTH)
    surname = models.CharField(t("Отчество"), max_length=CHAR_MAX_LENGTH, blank=True, null=True)
    date_joined = models.DateTimeField(t("Дата регистрации"), auto_now_add=True)
    role = models.CharField(t("Роль"), max_length=20, choices=UserRole.choices, default=UserRole.USER)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["phone"]

    objects = UserManager()

    class Meta:
        ordering = ("-date_joined",)
        verbose_name = t("Пользователь")
        verbose_name_plural = t("Пользователи")
