from horizon import tabs

from openstack_dashboard.dashboards.enterprisesupport.supportoverview \
    import tabs as mydashboard_tabs


class IndexView(tabs.TabbedTableView):
    tab_group_class = mydashboard_tabs.MypanelTabs
    template_name = 'enterprisesupport/supportoverview/index.html'

    def get_data(self, request, context, *args, **kwargs):
        # Add data to the context here...
        return context
