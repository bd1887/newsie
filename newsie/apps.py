from django.apps import AppConfig

class NewsieConfig(AppConfig):
    name = 'newsie'

# Runs startup function (if necessary)
    def ready(self):
        pass