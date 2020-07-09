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
######app_name='dynamic'
urlpatterns = [
    # Examples:
    url(r'^$', manneh.views.manneh, name='home'),
    url(r'^create$', manneh.views.mannehformview, name='create'),
    url(r'^create2$', manneh.views.mannehformview2, name='create2'),
    url(r'^lab$', manneh.views.labeh_list_view, name='lab'),
    url(r'^backend$', manneh.views.backend, name='backend'),
    url(r'^backend2$', manneh.views.backend2, name='backend2'),
    url(r'^backend3$', manneh.views.backend3, name='backend3'),
    url(r'^dynamic/(?P<myid>\d+)$', manneh.views.dynamic, name='dynamic'),
    url(r'^delete/(?P<d_id>\d+)$', manneh.views.deleting, name='delete'),]
