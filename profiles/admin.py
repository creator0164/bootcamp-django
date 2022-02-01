from django.contrib import admin
from django.db import models
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'content')


admin.site.register(Profile, ProfileAdmin)
