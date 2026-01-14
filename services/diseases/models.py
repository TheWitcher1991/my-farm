from packages.kernel.adapters import ModelAdapter
from packages.kernel.utils import t


class Disease(ModelAdapter):

    class Meta:
        ordering = ("-created_at",)
        verbose_name = t("Болезнь")
        verbose_name_plural = t("Болезни")
