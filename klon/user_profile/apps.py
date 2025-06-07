from django.apps import AppConfig



class UserProfileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'klon.user_profile'

    def ready(self):
        import klon.user_profile.signals