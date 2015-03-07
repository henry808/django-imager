from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from imager.settings import STATIC_URL
import datetime
import os

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
        return query.filter(is_active__exact=True)


# class FollowersManager(models.Manager):
#     """
#     """
#     def get_queryset(self):
#         query = ImagerProfile.objects.all()
#         return query


@python_2_unicode_compatible
class ImagerProfile(models.Model):
    """Thise sets up a User Profile with privacy settings."""
    PRIVACY_CHOICES = (
        ('PR', 'Private'),
        ('PU', 'Public'),
    )

    # new fields
    picture = models.ImageField(default=os.path.join(
        STATIC_URL,
        'images',
        'default_profile_image.jpg'))
    birthday = models.DateField(default=datetime.date.today())
    phone = models.IntegerField(max_length=11, blank=True, null=True)

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
    user = models.OneToOneField(User, related_name='profile')
    is_active = models.BooleanField(default=True)
    followers = models.ManyToManyField('self', related_name='following')

    objects = models.Manager()
    active = ActiveProfileManager()
    # followers = FollowersManager()

    def __str__(self):
        return self.user.username

    def follow(self, other):
        pass

    def unfollow(self, other):
        pass
