from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from rooms_cms_integration.models import RoomsPluginModel
from django.utils.translation import ugettext as _


class RoomPluginPublisher(CMSPluginBase):
    model = RoomsPluginModel  # model where plugin data are saved
    module = _("Rooms")
    name = _("Room Plugin")  # name of the plugin in the interface
    render_template = "rooms_cms_integration/room_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(RoomPluginPublisher)  # register the plugin