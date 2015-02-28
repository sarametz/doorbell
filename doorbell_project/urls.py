from django.conf.urls import patterns, include, url
from django.contrib import admin
from doorbell.views import *

urlpatterns = patterns('',
    url(r'^$', 'doorbell.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
)
