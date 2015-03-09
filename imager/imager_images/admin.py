from django.contrib import admin
from django.db import models
from imager_images.models import Photo, Album


class PhotoAdmin(admin.ModelAdmin):
    list_filter = ['size']
    fieldsets = [
        ('Info', {'fields': ['user', 'title', 'description']}),
        ('Upload image', {'fields': ['picture']}),
        ('Date information', {'fields': ['date_uploaded', 'date_modified', 'date_published']}),
        ('Published', {'fields': ['published']}),

    ]
    readonly_fields = ('date_uploaded', 'date_modified', 'date_published')
    list_display = ('user', 'title', 'picture', 'published', 'date_uploaded', 'date_modified', 'date_published', 'size')

    def size(self, obj):
        image_size = models.Field(obj.picture.size)
        return image_size
    size.short_description = 'File size'
    size.admin_order = 'size'


class AlbumAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Info', {'fields': ['user', 'title', 'description']}),
        ('Date information', {'fields': ['date_uploaded', 'date_modified', 'date_published']}),
        ('Published', {'fields': ['published']})
    ]
    readonly_fields = ('date_uploaded', 'date_modified', 'date_published')
    list_display = ('user', 'title', 'cover_photo', 'published')


# Register your models here.
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Album, AlbumAdmin)
