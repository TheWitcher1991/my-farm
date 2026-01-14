from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from feeds.models import Feed
from feeds.usecases import feed_cache_use_case


@receiver(post_save, sender=Feed)
@receiver(post_delete, sender=Feed)
def clear_feed_cache_signal(sender, instance: Feed, **kwargs):
    feed_cache_use_case.cache_queryset_key()
    feed_cache_use_case.delete_object_cache(instance.id)
    feed_cache_use_case.delete_retrieve_cache(instance.id)
