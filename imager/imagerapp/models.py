from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
import datetime

# Already in User:
# username,
# password,
# date joined,
# email address,
# active,


class ActiveProfileManager(models.Manager):
    """Profile Manager"""
    def get_queryset(self):
        """gets"""
        query = super(ActiveProfileManager, self).get_queryset()
        return query.filter(user__is_active__exact=True)


# @python_2_unicode_compatible
class ImagerProfile(models.Model):
    """Thise sets up a User Profile with privacy settings."""
    PRIVACY_CHOICES = (
        ('PR', 'Private'),
        ('PU', 'Public'),
    )

    # new fields
    picture = models.ImageField()
    birthday = models.DateField(default=datetime.date.today())
    phone = models.IntegerField(max_length=11)

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

    objects = models.Manager()
    active = ActiveProfileManager()


    def is_active(self):
        return self.user.is_active

    def __str__(self):
        return self.user.username

# create and delete
# post_save.connect(create_profile, send=User)
# pre_delete.connect(delete_user, sender=ImagerProfile)

