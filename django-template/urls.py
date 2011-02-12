# -*- encoding: utf-8 -*-
from django.conf import settings
from django.conf.urls.defaults import *

from django.contrib import admin

from django.views.generic.simple import direct_to_template

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^sentry/', include('sentry.urls')),
    (r'^sentry/', include('test_app.urls')),


    url(r'^test/$', direct_to_template,
        { 'template': 'test.html' },
        name='test'),
)

if settings.DEBUG:
    urlpatterns += patterns('', 
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': settings.MEDIA_ROOT}),
    )
