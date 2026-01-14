from django.apps import AppConfig


class DiseasesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "diseases"
    label = "diseases"

    def ready(self):
        import diseases.signals
