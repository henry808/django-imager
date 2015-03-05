from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from imagerapp.models import ImagerProfile


@receiver(post_save, sender=User)
def imager_signal_handler(sender, **kwargs):
    # import pdb; pdb.set_trace()
    new = ImagerProfile()
    new.user = kwargs['instance']
    new.is_active = kwargs['instance'].is_active

    # Prevent an already existing profile from trying to save anew
    # TODO: else, update profile accordingly
    if not ImagerProfile.objects.all().filter(user_id=new.user):
        new.save()
