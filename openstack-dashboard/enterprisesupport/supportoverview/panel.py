from django.utils.translation import ugettext_lazy as _

import horizon
from openstack_dashboard.dashboards.enterprisesupport import dashboard

class Supportoverview(horizon.Panel):
    name = _("Support overview")
    slug = "supportoverview"
    permissions = ('openstack.roles.admin')

dashboard.Enterprisesupport.register(Supportoverview)
