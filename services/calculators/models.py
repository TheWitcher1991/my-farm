from django.db import models

from config.settings import CHAR_MAX_LENGTH
from packages.kernel.adapters import ModelAdapter
from packages.kernel.types import BatchUnit
from packages.kernel.utils import t


class WeightCalculation(ModelAdapter):
    title = models.CharField(t("Название"), max_length=CHAR_MAX_LENGTH)
    chest_girth = models.FloatField(t("Обхват груди"))
    body_length = models.FloatField(t("Косая длина туловища"))
    result_weight = models.FloatField(t("Живая масса"))
    user = models.ForeignKey(
        to="users.User", on_delete=models.CASCADE, verbose_name=t("Автор"), related_name="weight_calculations"
    )

    class Meta:
        ordering = ("-created_at",)
        verbose_name = t("Калькулятор массы тела")
        verbose_name_plural = t("Калькуляторы массы тела")

    def __str__(self):
        return self.title


class RationCalculation(ModelAdapter):
    title = models.CharField(t("Название"), max_length=CHAR_MAX_LENGTH)
    user = models.ForeignKey(
        to="users.User", on_delete=models.CASCADE, verbose_name=t("Автор"), related_name="ration_calculations"
    )

    class Meta:
        ordering = ("-created_at",)
        verbose_name = t("Калькулятор рациона")
        verbose_name_plural = t("Калькуляторы рациона")

    def __str__(self):
        return self.title


class RationCalculationFeed(ModelAdapter):
    ration = models.ForeignKey(RationCalculation, on_delete=models.CASCADE, related_name="feeds")
    feed = models.ForeignKey(
        to="feeds.Feed", on_delete=models.CASCADE, verbose_name=t("Корм"), related_name="ration_calculations"
    )
    quantity = models.PositiveIntegerField(t("Количество"))
    unit = models.CharField(t("Единица измерения"), choices=BatchUnit, default=BatchUnit.KG, max_length=32)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = t("Корм рациона")
        verbose_name_plural = t("Корма рациона")

    def __str__(self):
        return f"{self.ration} - {self.feed}"
