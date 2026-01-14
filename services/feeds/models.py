from packages.kernel.adapters import ModelAdapter
from packages.kernel.utils import t


class Feed(ModelAdapter):

    class Meta:
        ordering = ("-created_at",)
        verbose_name = t("Корм")
        verbose_name_plural = t("Корма")
