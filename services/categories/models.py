from packages.kernel.adapters import ModelAdapter
from packages.kernel.utils import t


class Category(ModelAdapter):

    class Meta:
        ordering = ("-created_at",)
        verbose_name = t("Категория")
        verbose_name_plural = t("Категории")
