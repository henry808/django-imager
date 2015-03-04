from django.db import models
from django.contrib.auth.models import User

# from django.db.models.signals import post_save, pre_delete

# Already in User:
# username,
# password,
# date joined,
# email address,
# active,


class ImagerProfile(models.Model):
    """Thise sets up a User Profile with privacy settings."""
    PRIVACY_CHOICES = (
        ('PR', 'Private'),
        ('PU', 'Public'),
    )

    # new fields
    picture = models.ImageField()
    birthday = models.DateField()
    phone = models.IntegerField(max_length=11)


    # privacy settings
    pic_privacy = models.CharField(max_length=1, choices=PRIVACY_CHOICES,
                                   default=('PR', 'Private'))
    birthday_privacy = models.CharField(max_length=1, choices=PRIVACY_CHOICES,
                                        default=('PR', 'Private'))
    phone_privacy = models.CharField(max_length=1, choices=PRIVACY_CHOICES,
                                     default=('PR', 'Private'))
    name_privacy = models.CharField(max_length=1, choices=PRIVACY_CHOICES,
                                    default=('PR', 'Private'))
    email_privacy = models.CharField(max_length=1, choices=PRIVACY_CHOICES,
                                     default=('PR', 'Private'))
    # associates profile to the User model
    user = models.OneToOneField(User)

    @classmethod
    def active(cls):
        """Returns all active users."""
        return User.objects.filter(is_active=True)
#   qs = self.get_queryset()
#   return qs.filter(associated)

    def is_active(self):
        return self.user.is_active

    def user(self):
        return self.user

    def __unicode__(self):
        return self.user

# create and delete 
# post_save.connect(create_profile, send=User)
# pre_delete.connect(delete_user, sender=ImagerProfile)

