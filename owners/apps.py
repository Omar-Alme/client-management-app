from django.apps import AppConfig


class OwnersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'owners'


def ready(self):
        from owners.signals import create_profile
        from django.contrib.auth.models import User
        post_save.connect(create_profile, sender=User)
        from owners.signals import save_profile
        post_save.connect(save_profile, sender=User)