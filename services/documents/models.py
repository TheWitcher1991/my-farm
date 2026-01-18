from django.core.validators import FileExtensionValidator
from django.db import models

from config.settings import CHAR_MAX_LENGTH, DOCUMENTS_ALLOWED_EXTENSIONS
from documents.types import DocumentViewType
from packages.framework.fields import S3PrivateFileField
from packages.kernel.adapters import ModelAdapter
from packages.kernel.types import DocumentStatus
from packages.kernel.utils import t


class Document(ModelAdapter):
    title = models.CharField(t("Название"), max_length=CHAR_MAX_LENGTH)
    description = models.TextField(t("Описание"), blank=True, null=True)
    status = models.CharField(t("Статус"), choices=DocumentStatus.choices, default=DocumentStatus.DRAFT, max_length=32)
    author = models.ForeignKey(
        to="users.User", on_delete=models.CASCADE, verbose_name=t("Автор"), related_name="articles"
    )
    file = S3PrivateFileField(
        t("Файл"),
        upload_to="documents",
        validators=[
            FileExtensionValidator(
                DOCUMENTS_ALLOWED_EXTENSIONS,
            )
        ],
        blank=True,
        null=True,
    )
    view_type = models.CharField(
        t("Тип"), choices=DocumentViewType.choices, default=DocumentViewType.STATIC, max_length=32
    )

    class Meta:
        ordering = ("-created_at",)
        verbose_name = t("Документ")
        verbose_name_plural = t("Документы")

    def __str__(self):
        return self.title
