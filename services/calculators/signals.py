from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from calculators.usecases import (
    RationCalculationUseCase,
    WeightCalculationUseCase,
    ration_calculation_use_case,
    weight_calculation_use_case,
)


@receiver(post_save, sender=WeightCalculationUseCase)
@receiver(post_delete, sender=WeightCalculationUseCase)
def clear_weight_calculation_cache_signal(sender, instance: WeightCalculationUseCase, **kwargs):
    weight_calculation_use_case.cache_queryset_key()
    weight_calculation_use_case.delete_object_cache(instance.id)
    weight_calculation_use_case.delete_retrieve_cache(instance.id)


@receiver(post_save, sender=RationCalculationUseCase)
@receiver(post_delete, sender=RationCalculationUseCase)
def clear_ration_calculation_signal(sender, instance: RationCalculationUseCase, **kwargs):
    ration_calculation_use_case.cache_queryset_key()
    ration_calculation_use_case.delete_object_cache(instance.id)
    ration_calculation_use_case.delete_retrieve_cache(instance.id)
