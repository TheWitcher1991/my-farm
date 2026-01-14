from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from diseases.models import Disease
from diseases.usecases import disease_cache_use_case


@receiver(post_save, sender=Disease)
@receiver(post_delete, sender=Disease)
def clear_disease_cache_signal(sender, instance: Disease, **kwargs):
    disease_cache_use_case.cache_queryset_key()
    disease_cache_use_case.delete_object_cache(instance.id)
    disease_cache_use_case.delete_retrieve_cache(instance.id)
