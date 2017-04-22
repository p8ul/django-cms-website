#-*- coding: utf-8 -*-
from django.contrib import admin

from .models import Amenities, Rooms


class ChoiceInline(admin.TabularInline):
    model = Amenities
    #readonly_fields = ('votes',)
    extra = 3


class RoomAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ['room_title','image','description']
        }),
    ]
    inlines = [ChoiceInline]
    list_display = ('room_title',)
    search_fields = ['room_title']

admin.site.register(Rooms, RoomAdmin)
admin.site.register(Amenities)
