# from django.dispatch import receiver
# from django.db.models.signals import pre_save
# from django.contrib.auth.models import User
# from imager_images.models import Photo, Album
# from django.core.exceptions import ObjectDoesNotExist
# import datetime
# from django.db import transaction


# # photo listener
# @receiver(pre_save, sender=Photo)
# def imager_signal_handler(sender, **kwargs):
#     photo_new = kwargs['instance']
#     photo_old = Photo.objects.get(photo_new)
#     # changed from not private anymore and there is a change
#     if (photo_new.published != Photo.PRIVATE) and (photo_old.published == Photo.PRIVATE):
#         photo_new.date_published = datetime.date.today()


# # Album listener
# @receiver(pre_save, sender=Album)
# def imager_signal_handler(sender, **kwargs):
#     album_new = kwargs['instance']
#     album_old = Album.objects.get(user_id=album_new.user)
#     # changed from not private anymore and there is a change
#     import pdb; pdb.set_trace()
#     if (album_new.published != Album.PRIVATE) and (album_old.published == Album.PRIVATE):
#         date = datetime.date(year=2010, month=10, day=10)
#         Album.objects.filter(pk=album_new.pk).update(date_published=date)
#         # transaction.commit()