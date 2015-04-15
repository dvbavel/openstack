from django.utils.translation import ugettext_lazy as _
from django.template import defaultfilters as filters

from horizon import tables
from horizon.utils import filters as utils_filters

from openstack_dashboard import api

class MyFilterAction(tables.FilterAction):
    name = "myfilter"

class InstancesTable(tables.DataTable):
    name = tables.Column("name", verbose_name=_("Name"))
    created = tables.Column("created", verbose_name=_("Created at"))
    createdby = tables.Clumn("user_id", verbose_name=_("Created by"))
    status = tables.Column("status", verbose_name=_("Status"))
    host = tables.Column("OS-EXT-SRV-ATTR:host", verbose_name=_("Host"))
    zone = tables.Column('availability_zone',
                          verbose_name=_("Availability Zone"))
    image_name = tables.Column('image_name', verbose_name=_("Image Name"))

    class Meta:
        name = "instances"
        verbose_name = _("Instances")
	table_actions = (MyFilterAction,)
