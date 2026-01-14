from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from documents.models import Document
from documents.usecases import document_cache_use_case


@receiver(post_save, sender=Document)
@receiver(post_delete, sender=Document)
def clear_document_cache_signal(sender, instance: Document, **kwargs):
    document_cache_use_case.cache_queryset_key()
    document_cache_use_case.delete_object_cache(instance.id)
    document_cache_use_case.delete_retrieve_cache(instance.id)
