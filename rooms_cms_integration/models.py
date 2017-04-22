from django.db import models
from cms.models import CMSPlugin
from rooms.models import Rooms


class RoomsPluginModel(CMSPlugin):
    rooms = models.ForeignKey(Rooms)

    def __unicode__(self):
        return self.rooms.room_title