from packages.kernel.adapters import ModelAdapter
from packages.kernel.utils import t


class Article(ModelAdapter):

    class Meta:
        ordering = ("-created_at",)
        verbose_name = t("Статья")
        verbose_name_plural = t("Статьи")
