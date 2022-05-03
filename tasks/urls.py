from django.urls import re_path
from .views import TasksHomeFormView, JobTemplateView, LongTaskCreateView


urlpatterns = [
    re_path(r'^$', TasksHomeFormView.as_view(), name='home'),
    re_path(r'^long/$', LongTaskCreateView.as_view(), name='long_tasks'),
    re_path(r'^job/(?P<job>[\d\w-]+)/$', JobTemplateView.as_view(), name='view_job'),
]
