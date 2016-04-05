# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from .views import SearchListView, BadgeDetailView, BadgeListView

urlpatterns = [
    url(r'^$', SearchListView.as_view(), name="search"),
    url(r'^list/$', BadgeListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w\d\-\_]+)/$', BadgeDetailView.as_view(), name='detail'),
]