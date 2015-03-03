from django.db import models

# Create your models here.



# Already in:
# username,
# password,
# date joined,
# email address,
# active,

class UserProfile(models.Model):
    PRIVACY_CHOICES = (
        ('PR', 'Private'),
        ('PU', 'Public'),
    )
    picture = models.CharField(max_length=200) # change this to image
    pic_privacy = models.CharField(max_length=1, choices=PRIVACY_CHOICES)
    birthday = models.DateField()
    birthday_privacy = models.CharField(max_length=1, choices=PRIVACY_CHOICES)
    phone = models.CharField(max_length=11)
    phone_privacy = models.CharField(max_length=1, choices=PRIVACY_CHOICES)
    name_privacy = models.CharField(max_length=1, choices=PRIVACY_CHOICES)
    email_privacy = models.CharField(max_length=1, choices=PRIVACY_CHOICES)


