import requests
from models import Task, ScheduledTask, ScheduledTaskInstance
from rq import get_current_job
from django_rq import job

@job
def get_url_words(url):
    # This creates a Task instance to save the job instance and job result
    job = get_current_job()

    task = Task.objects.create(
        job_id=job.get_id(),
        name=url
    )
    response = requests.get(url)
    task.result = len(response.text)
    task.save()
    return task.result


@job
def scheduled_get_url_words(url):
    """
    This creates a ScheduledTask instance for each group of 
    scheduled task - each time this scheduled task is run
    a new instance of ScheduledTaskInstance will be created
    """
    job = get_current_job()

    task, created = ScheduledTask.objects.get_or_create(
        job_id=job.get_id(),
        name=url
    )
    response = requests.get(url)
    response_len = len(response.text)
    ScheduledTaskInstance.objects.create(
        scheduled_task=task,
        result = response_len,
    )
    return response_len
