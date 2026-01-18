from typing import NewType

from django.db import models

from packages.kernel.utils import t

DocumentId = NewType("DocumentId", int)


class DocumentViewType(models.TextChoices):
    STATIC = "static", t("Статический документ")
    DYNAMIC = "dynamic", t("Динамический документ")
