# -*- encoding: utf-8 -*-

from django.conf.urls.defaults import *

from views import TestView

urlpatterns = patterns('',
    url(r'^test/$', TestView.as_view(), name='test'),
)
