from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/rq/', include('django_rq_dashboard.urls')),
    # Enable the django-rq statistics
    url(r'^rq/', include('django_rq.urls')),

    url(r'', include('tasks.urls')),
]
