from django.db import models
import requests
from rq import get_current_job


# Create your models here.
class Task(models.Model):
    created_on = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=128)
    job_id = models.CharField(max_length=128)
    result = models.CharField(max_length=128, blank=True, null=True)

