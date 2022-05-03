from django.urls import include, re_path
from django.contrib import admin

urlpatterns = [

    re_path(r'^admin/', admin.site.urls),
    re_path(r'^rq/', include('django_rq.urls')),
    re_path(r'', include('tasks.urls')),
]
