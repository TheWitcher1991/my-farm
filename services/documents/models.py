from packages.kernel.adapters import ModelAdapter
from packages.kernel.utils import t


class Document(ModelAdapter):

    class Meta:
        ordering = ("-created_at",)
        verbose_name = t("Документ")
        verbose_name_plural = t("Документы")
