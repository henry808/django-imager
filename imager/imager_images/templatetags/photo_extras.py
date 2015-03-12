from django import template
from imager_images.models import Photo
from django.db.models import Q


register = template.Library()

# Custom filter, return photos that are public, shared, or belong to a logged in user
@register.filter
def viewable(self, user):
    return Photo.objects.filter(
        Q(user=user) |
        Q(published=Photo.SHARED) |
        Q(published=Photo.PUBLIC)
        )

# Return photos belonging only to one user.
@register.filter
def viewable_user(self, user):
    return Photo.objects.filter(Q(user=user))
