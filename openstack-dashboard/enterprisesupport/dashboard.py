from django.utils.translation import ugettext_lazy as _

import horizon


class enterprisesupportgroup(horizon.PanelGroup):
    slug = "enterprisesupportgroup"
    name = _("Enterprise Support Group")
    panels = ('supportoverview',)

class Enterprisesupport(horizon.Dashboard):
    name = _("Support Center")
    slug = "enterprisesupport"
    panels = (enterprisesupportgroup,)  # Add your panels here.
    default_panel = 'supportoverview'  # Specify the slug of the dashboard's default panel.


horizon.register(Enterprisesupport)
