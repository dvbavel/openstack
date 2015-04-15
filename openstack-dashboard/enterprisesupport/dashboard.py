from django.utils.translation import ugettext_lazy as _

import horizon


class Enterprisesupport(horizon.Dashboard):
    name = _("Support Center")
    slug = "enterprisesupport"
    panels = ()  # Add your panels here.
    default_panel = ''  # Specify the slug of the dashboard's default panel.


horizon.register(Enterprisesupport)
