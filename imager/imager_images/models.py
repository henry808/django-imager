from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Photo(models.Model):
    user = models.ForeignKey(User, related_name='photos')
    picture = models.ImageField()
    date_uploaded = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    # TODO: change date_published to only write when an image is shared
    date_published = models.DateField(blank=True, null=True)

    title = models.CharField(max_length=(63), blank=True)
    description = models.TextField(max_length=(255), blank=True)

    PRIVATE = 'PR'
    SHARED = 'SH'
    PUBLIC = 'PU'

    PRIVACY_CHOICES = (
        (PRIVATE, 'Private'),
        (SHARED, 'Shared'),
        (PUBLIC, 'Public'),
    )

    published = models.CharField(max_length=2, choices=PRIVACY_CHOICES, default=PRIVATE)

    def size(self):
        return self.picture.size



class Album(models.Model):
    #relations
    user = models.ForeignKey(User, related_name='albums')
    photos = models.ManyToManyField(Photo, related_name='albums', null=True, blank=True)
    cover_photo = models.ForeignKey(Photo, related_name='+', blank=True, null=True)

    date_uploaded = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    # TODO: change date_published to only write when an image is shared
    date_published = models.DateField(auto_now=True)

    title = models.CharField(max_length=(63))
    description = models.TextField(max_length=(255), blank=True)

    PRIVATE = 'PR'
    SHARED = 'SH'
    PUBLIC = 'PU'

    PRIVACY_CHOICES = (
        (PRIVATE, 'Private'),
        (SHARED, 'Shared'),
        (PUBLIC, 'Public'),
    )

    published = models.CharField(max_length=2, choices=PRIVACY_CHOICES, default=PRIVATE)
