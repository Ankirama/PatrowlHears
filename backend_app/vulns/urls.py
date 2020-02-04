from django.urls import path
from . import apis


urlpatterns = [
    path('<vuln_id>/exploits', apis.get_exploits, name='get_exploits'),
    path('<vuln_id>/threats', apis.get_threats, name='get_threats'),
    # path('cve/<cve_id>/info', apis.get_metadata_cve, name='get_metadata_cve'),
    # path('cve/<cve_id>/refresh', apis.refresh_metadata_cve, name='refresh_metadata_cve'),
    # path('cve/refresh_monitored', apis.refresh_monitored_cves_async, name='refresh_monitored_cves_async'),
]
