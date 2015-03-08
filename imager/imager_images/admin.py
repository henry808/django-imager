from django.contrib import admin
from imager_images.models import Photo, Album
import gettext



class SizeListFilter(admin.SimpleListFilter):
    title = gettext.gettext('File size')

    parameter_name = 'size_category'

    def lookups(self, request, model_admin):
        return (
                ('<=1MB', gettext.gettext('<= 1MB')),
                ('<=10MB', gettext.gettext('<= 10 MB')),
                ('<=100MB', gettext.gettext('<= 100 MB')),
                ('>100MB', gettext.gettext('> 100 MB'))
            )
    def queryset(self, request, queryset):

        if self.value() == '<=1MB':
            return queryset.filter(picture__size=(0, 1000))
        if self.value() == '<=10MB':
            return queryset.filter(picture__size=(0, 10000))
        if self.value() == '<=100MB':
            return queryset.filter(picture__size=(0, 100000))
        else:
            return queryset.filter(picture__size=(100000, float('inf')))

class PhotoAdmin(admin.ModelAdmin):
    # allows partial matches
    search_fields = ['user__username',
                     'user__first_name',
                     'user__last_name',
                     'user__email']
    list_filter = ['user__username', SizeListFilter]
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
    # allows partial matches
    search_fields = ['user__username',
                     'user__first_name',
                     'user__last_name',
                     'user__email']
    fieldsets = [
        ('Info', {'fields': ['user', 'title', 'description']}),
        ('Date information', {'fields': ['date_uploaded', 'date_modified', 'date_published']}),
        ('Published', {'fields': ['published']})
    ]
    readonly_fields = ('date_uploaded', 'date_modified', 'date_published')
    list_display = ('user', 'title', 'cover_photo', 'published')
       

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Album, AlbumAdmin)
