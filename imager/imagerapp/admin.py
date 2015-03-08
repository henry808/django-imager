from django import forms
from django.contrib import admin
from django.contrib.auth.models import User
from imagerapp.models import ImagerProfile


class ProfileInLine(admin.TabularInline):
    model = ImagerProfile


class UserAdmin(admin.ModelAdmin):
    inlines = [
        ProfileInLine
    ]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(ImagerProfile)
