from django.core.validators import FileExtensionValidator
from django.db import models

from config.settings import CHAR_MAX_LENGTH, IMAGE_ALLOWED_EXTENSIONS
from packages.framework.fields import S3PrivateFileField
from packages.kernel.adapters import ModelAdapter
from packages.kernel.types import DocumentStatus
from packages.kernel.utils import t


class Article(ModelAdapter):
    title = models.CharField(t("Название"), max_length=CHAR_MAX_LENGTH)
    content = models.TextField(t("Описание"), blank=True, null=True)
    category = models.ForeignKey(
        to="categories.Category", on_delete=models.CASCADE, verbose_name=t("Категория"), related_name="articles"
    )
    status = models.CharField(t("Статус"), choices=DocumentStatus.choices, default=DocumentStatus.DRAFT, max_length=32)
    cover = S3PrivateFileField(
        t("Обложка"),
        upload_to="covers",
        validators=[
            FileExtensionValidator(
                IMAGE_ALLOWED_EXTENSIONS,
            )
        ],
        blank=True,
        null=True,
    )

    author = models.ForeignKey(
        to="users.User", on_delete=models.CASCADE, verbose_name=t("Автор"), related_name="articles"
    )

    class Meta:
        ordering = ("-created_at",)
        verbose_name = t("Статья")
        verbose_name_plural = t("Статьи")

    def __str__(self):
        return self.title
