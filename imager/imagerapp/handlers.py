from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User


@receiver(post_save, sender=User)
def imager_signal_handler(sender, **kwargs):
    print sender
    print kwargs
