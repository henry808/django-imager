from django.contrib import admin
from imager_images.models import Photo, Album


class PhotoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Info', {'fields': ['user', 'title', 'description']}),
        ('Date information', {'fields': ['date_uploaded', 'date_modified', 'date_published']}),
        ('Published', {'fields': ['published']})
    ]
    readonly_fields = ('date_uploaded', 'date_modified', 'date_published')

# Register your models here.
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Album)
