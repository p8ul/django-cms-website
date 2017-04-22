from django.utils.translation import ugettext_lazy as _
from cms.toolbar_pool import toolbar_pool
from cms.toolbar_base import CMSToolbar
from cms.utils.urlutils import admin_reverse
from rooms.models import Rooms


class RoomToolbar(CMSToolbar):
    supported_apps = (
        'rooms',
        'rooms_cms_integration',
    )

    watch_models = [Rooms]

    def populate(self):
        if not self.is_current_app:
            return

        menu = self.toolbar.get_or_create_menu('rooms-app', _('Rooms'))

        menu.add_sideframe_item(
            name=_('Rooms list'),
            url=admin_reverse('rooms_rooms_changelist'),
        )

        menu.add_modal_item(
            name=_('Add new Room'),
            url=admin_reverse('rooms_rooms_add'),
        )


toolbar_pool.register(RoomToolbar)  # register the toolbar