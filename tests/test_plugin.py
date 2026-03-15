

def test_plugin_import():
    from dashboard_plugin import DashboardPlugin

    plugin = DashboardPlugin()
    assert plugin.name == "dashboard"
