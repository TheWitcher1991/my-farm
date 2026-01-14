from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from categories.models import Category
from categories.usecases import category_cache_use_case


@receiver(post_save, sender=Category)
@receiver(post_delete, sender=Category)
def clear_category_cache_signal(sender, instance: Category, **kwargs):
    category_cache_use_case.cache_queryset_key()
    category_cache_use_case.delete_object_cache(instance.id)
    category_cache_use_case.delete_retrieve_cache(instance.id)
