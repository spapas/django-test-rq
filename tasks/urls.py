from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import TasksHomeFormView


urlpatterns = patterns('',
    url(r'^$', TasksHomeFormView.as_view(), name='home'),
)
