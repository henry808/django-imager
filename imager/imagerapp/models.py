from django.db import models
from django.contrib.auth.models import User

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

    picture = models.ImageField()
    pic_privacy = models.CharField(max_length=1, choices=PRIVACY_CHOICES)
    birthday = models.DateField()
    birthday_privacy = models.CharField(max_length=1, choices=PRIVACY_CHOICES)
    phone = models.IntegerField(max_length=11)
    phone_privacy = models.CharField(max_length=1, choices=PRIVACY_CHOICES)
    name_privacy = models.CharField(max_length=1, choices=PRIVACY_CHOICES)
    email_privacy = models.CharField(max_length=1, choices=PRIVACY_CHOICES)

    user = models.OneToOneField(User)

    @staticmethod
    def active():
        """Returns all active users."""
        return User.objects.filter(is_active=True)

    def is_active(self):
        return self.user.is_active

    def user(self):
        return self.user

    def __unicode__(self):
        return self.user
