# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
import frontpage.views as views

urlpatterns = patterns(
    '',
    url(r'^$', views.Index.as_view(), name='home'),
    url(r'^index/$', views.Index.as_view(), name='index'),
)
