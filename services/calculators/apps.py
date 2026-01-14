from django.apps import AppConfig


class CalculatorsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "calculators"
    label = "calculators"

    def ready(self):
        import calculators.signals
