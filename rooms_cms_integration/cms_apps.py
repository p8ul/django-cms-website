from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class RoomsApphook(CMSApp):
    app_name = "rooms"
    name = _("Rooms Application")

    def get_urls(self, page=None, language=None, **kwargs):
        return ["rooms.urls"]


apphook_pool.register(RoomsApphook)  # register the application