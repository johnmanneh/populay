"""
Definition of urls for DjangoWebProject2.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'', include('manneh.urls')),
    url(r'^blog/', include('blog.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
]
