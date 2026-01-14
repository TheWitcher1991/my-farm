from packages.kernel.adapters import ModelAdapter
from packages.kernel.utils import t


class Calculator(ModelAdapter):

    class Meta:
        ordering = ("-created_at",)
        verbose_name = t("Калькулятор")
        verbose_name_plural = t("Калькуляторы")
