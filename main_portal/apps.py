from django.apps import AppConfig


class MainPortalConfig(AppConfig):
    name = 'main_portal'

    def ready(self):
        # import main_portal.signals
        pass