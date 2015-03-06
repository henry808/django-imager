from django.apps import AppConfig


class ImagerAppConfig(AppConfig):

    name = 'imagerapp'
    verbose_name = 'Imager App'

    def ready(self):
        import imagerapp.handlers
