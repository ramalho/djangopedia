from django.conf.urls.defaults import *

from django.contrib import admin
from django.contrib import databrowse

admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^lab/', include('lab.foo.urls')),

    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^admin/', include(admin.site.urls)),

    (r'^db/(.*)', databrowse.site.root),

)
