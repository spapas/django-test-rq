import requests
from models import Task
from rq import get_current_job
from django_rq import job

@job
def work(url):
    job = get_current_job()

    t = Task.objects.create(
        job_id=job.get_id(),
        name=url
    )
    r = requests.get(url)
    t.result = len(r.text)
    t.save()
    return t.result