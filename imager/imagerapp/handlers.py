from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save)
def imager_signal_handler(sender, **kwargs):
    print sender
    print kwargs
