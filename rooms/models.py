#-*- coding: utf-8 -*-
from django.db import models


class Rooms(models.Model):
    room_title = models.CharField(max_length=200)
    image = models.FileField(max_length=300,default='media/noimage.jpg')
    description = models.TextField( null=True, blank=True)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.room_title


class Amenities(models.Model):
    room = models.ForeignKey(Rooms)
    amenity_text = models.CharField(max_length=200)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.amenity_text
