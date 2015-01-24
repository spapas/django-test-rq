from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import TasksHomeFormView, JobTemplateView


urlpatterns = patterns('',
    url(r'^$', TasksHomeFormView.as_view(), name='home'),
    url(r'^job/(?P<job>[\d\w-]+)/$', JobTemplateView.as_view(), name='view_job'),
)
