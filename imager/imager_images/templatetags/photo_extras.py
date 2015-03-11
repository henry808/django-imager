from django import template
from imager_images.models import Photo
from django.db.models import Q


register = template.Library()

SHARED = 'SH'
PUBLIC = 'PU'


# Custom filter, return photos that are public, shared, or belong to a logged in user
@register.filter
def viewable(self, user):
    return Photo.objects.filter(
        Q(user=user) |
        Q(published=SHARED) |
        Q(published=PUBLIC)
        ).order_by('date_published')
