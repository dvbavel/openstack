from django.utils.translation import ugettext_lazy as _

import horizon
from openstack_dashboard.dashboards.enterprisesupport import dashboard

class Supportlinks(horizon.Panel):
    name = _("Support links")
    slug = "supportlinks"


dashboard.Enterprisesupport.register(Supportlinks)
