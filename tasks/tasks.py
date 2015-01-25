import requests
from models import Task, ScheduledTask, ScheduledTaskInstance
from rq import get_current_job
from django_rq import job

@job
def get_url_words(url):
    job = get_current_job()

    t = Task.objects.create(
        job_id=job.get_id(),
        name=url
    )
    r = requests.get(url)
    t.result = len(r.text)
    t.save()
    return t.result


@job
def scheduled_get_url_words(url):
    job = get_current_job()

    t, created = ScheduledTask.objects.get_or_create(
        job_id=job.get_id(),
        name=url
    )
    r = requests.get(url)

    ScheduledTaskInstance.objects.create(
        scheduled_task=t,
        result = len(r.text),
    )
    return len(r.text)
