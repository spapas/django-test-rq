from django.db import models
import requests
from rq import get_current_job


class Task(models.Model):
    # A model to save information about an asynchronous task
    created_on = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=128)
    job_id = models.CharField(max_length=128)
    result = models.CharField(max_length=128, blank=True, null=True)


class ScheduledTask(models.Model):
    # A model to save information about a scheduled task
    created_on = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=128)
    # A scheduled task has a common job id for all its occurences
    job_id = models.CharField(max_length=128) 


class ScheduledTaskInstance(models.Model):
    # A model to save information about instances of a scheduled task
    scheduled_task = models.ForeignKey('ScheduledTask')
    created_on = models.DateTimeField(auto_now_add=True)
    result = models.CharField(max_length=128, blank=True, null=True)