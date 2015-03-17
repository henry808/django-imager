from django.contrib import admin
from imager_images.models import Photo, Album


class PhotoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Info', {'fields': ['user', 'title', 'description']}),
        ('Upload image', {'fields': ['picture']}),
        ('Date information', {'fields': ['date_uploaded', 'date_modified', 'date_published']}),
        ('Published', {'fields': ['published']}),

    ]
    readonly_fields = ('date_uploaded', 'date_modified', 'date_published')
    list_display = ('user', 'title', 'picture', 'published', 'date_uploaded', 'date_modified', 'date_published', 'size')

    def size(self, obj):
        return obj.picture.size
    size.short_description = 'File size'
    size.admin_order = 'size'


class AlbumAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Info', {'fields': ['user', 'title', 'description']}),
        ('Date information', {'fields': ['date_uploaded', 'date_modified', 'date_published']}),
        ('Published', {'fields': ['published']}),
        ('Cover Photo', {'fields': ['cover_photo']}),
    ]
    readonly_fields = ('date_uploaded', 'date_modified', 'date_published')
    list_display = ('user', 'title', 'cover_photo', 'published')


# Register your models here.
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Album, AlbumAdmin)
