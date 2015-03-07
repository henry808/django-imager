from django.db import models


# Create your models here.
class Photo(models.Model):
    picture = models.ImageField()
    date_uploaded = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    # TODO: change date_published to only write when an image is shared
    date_published = models.DateField(auto_now=True)

    title = models.CharField(max_length(50))
    description = models.CharField(max_length(300), blank=True, null=True)

    published = models.CharField(max_length=2, choices=PRIVACY_CHOICES, default=PRIVATE)

    PRIVATE = 'PR'
    SHARED = 'SH'
    PUBLIC = 'PU'

    PRIVACY_CHOICES = (
        (PRIVATE, 'Private'),
        (SHARED, 'Shard')
        (PUBLIC, 'Public'),
    )


class Album(models.Model):
    pass
