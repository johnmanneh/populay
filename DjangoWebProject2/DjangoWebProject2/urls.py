"""
Definition of urls for DjangoWebProject2.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

import manneh.views
import manneh.forms
# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', manneh.views.manneh, name='home'),
    url(r'^create$', manneh.views.mannehformview, name='create'),
    url(r'^create2$', manneh.views.mannehformview2, name='create2'),
    url(r'^backend$', manneh.views.backend, name='backend'),
    url(r'^backend2$', manneh.views.backend2, name='backend2'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
