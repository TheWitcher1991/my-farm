from django.core.validators import FileExtensionValidator
from django.db import models

from config.settings import CHAR_MAX_LENGTH, IMAGE_ALLOWED_EXTENSIONS
from packages.framework.fields import S3PrivateFileField
from packages.kernel.adapters import ModelAdapter
from packages.kernel.utils import t


class Feed(ModelAdapter):
    title = models.CharField(t("Название"), max_length=CHAR_MAX_LENGTH)
    description = models.TextField(t("Описание"), blank=True, null=True)
    image = S3PrivateFileField(
        t("Изображение"),
        upload_to="feeds",
        validators=[
            FileExtensionValidator(
                IMAGE_ALLOWED_EXTENSIONS,
            )
        ],
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ("-created_at",)
        verbose_name = t("Корм")
        verbose_name_plural = t("Корма")
