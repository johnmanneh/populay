"""
Definition of urls for DjangoWebProject2.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

import blog.views as html_view

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()
######app_name='dynamic'
urlpatterns = [
    # Examples:
    url(r'^$', html_view.home, name='blog'),
    url(r'^$', html_view.about, name='about'),

    ]