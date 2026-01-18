from django.db import models

from config.settings import CHAR_MAX_LENGTH
from packages.kernel.adapters import ModelAdapter
from packages.kernel.utils import t


class Feed(ModelAdapter):
    title = models.CharField(t("Название"), max_length=CHAR_MAX_LENGTH)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = t("Корм")
        verbose_name_plural = t("Корма")
