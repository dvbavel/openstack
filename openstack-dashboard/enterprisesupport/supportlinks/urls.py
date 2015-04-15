from django.conf.urls import patterns
from django.conf.urls import url

from openstack_dashboard.dashboards.enterprisesupport.supportlinks.views \
    import supportlinksview


urlpatterns = patterns(
    '',
    url(r'^$', supportlinksview.as_view(), name='index'),
)
