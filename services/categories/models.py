from django.db import models

from config.settings import CHAR_MAX_LENGTH
from packages.kernel.adapters import ModelAdapter
from packages.kernel.utils import t


class Category(ModelAdapter):
    title = models.CharField(t("Название"), max_length=CHAR_MAX_LENGTH)
    description = models.TextField(t("Описание"), blank=True, null=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = t("Категория")
        verbose_name_plural = t("Категории")

    def __str__(self):
        return self.title
