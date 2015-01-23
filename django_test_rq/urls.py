from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^rq/', include('django_rq.urls')),

    url(r'', include('tasks.urls')),
)
