from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from imagerapp.models import ImagerProfile


@receiver(post_save, sender=User)
def imager_signal_handler(sender, **kwargs):
    new = ImagerProfile()
    new.save()
    print
    print sender
    print kwargs
    print
    print
    print
