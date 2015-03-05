from django.db import models
from django.contrib.auth.models import User
import datetime
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
    birthday = models.DateField(default=datetime.date.today())
    phone = models.IntegerField(max_length=11, blank=True)

    # privacy settings
    pic_privacy = models.CharField(max_length=2, choices=PRIVACY_CHOICES,
                                   default='PR')
    birthday_privacy = models.CharField(max_length=2, choices=PRIVACY_CHOICES,
                                        default='PR')
    phone_privacy = models.CharField(max_length=2, choices=PRIVACY_CHOICES,
                                     default='PR')
    name_privacy = models.CharField(max_length=2, choices=PRIVACY_CHOICES,
                                    default='PR')
    email_privacy = models.CharField(max_length=2, choices=PRIVACY_CHOICES,
                                     default='PR')
    # associates profile to the User model
    user = models.OneToOneField(User)
    # import pdb; pdb.set_trace()
    # need to: set is so that it grabs the value of user.is_active dynamically
    # at creation as well as change in user.is_active
    # is_active = models.BooleanField(default=True)

    @staticmethod
    def active():
        """Returns all active users."""
        return User.objects.all().filter(is_active=True)
#   qs = self.get_queryset()
#   return qs.filter(associated)

    @property
    def is_active(self):
        self.is_active = self.user.is_active
        return self.is_active

    def __unicode__(self):
        return self.user.username

# create and delete
# post_save.connect(create_profile, send=User)
# pre_delete.connect(delete_user, sender=ImagerProfile)

