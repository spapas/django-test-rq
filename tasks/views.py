from django.conf import settings
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView, CreateView
from django.views.generic import TemplateView
from .forms import TaskForm
from .tasks import get_url_words, scheduled_get_url_words, long_runnig_task
from .models import Task, ScheduledTask, LongTask
from rq.job import Job
from rq import Worker, Queue
import django_rq
from django.utils import timezone

class TasksHomeFormView(FormView):
    """
    A class that displays a form to read a url to read its contents and if the job
    is to be scheduled or not and information about all the tasks and scheduled tasks.

    When the form is submitted, the task will be either scheduled based on the
    parameters of the form or will be just executed asynchronously immediately.
    """
    form_class = TaskForm
    template_name = 'tasks_home.html'
    success_url = '/'

    def form_valid(self, form):
        url = form.cleaned_data['url']
        schedule_times = form.cleaned_data.get('schedule_times')
        schedule_interval = form.cleaned_data.get('schedule_interval')

        if schedule_times and schedule_interval:
            # Schedule the job with the form parameters
            scheduler = django_rq.get_scheduler('default')
            job = scheduler.schedule(
                scheduled_time=timezone.now(),
                func=scheduled_get_url_words,
                args=[url],
                interval=schedule_interval,
                repeat=schedule_times,
            )
        else:
            # Just execute the job asynchronously
            get_url_words.delay(url)
        return super(TasksHomeFormView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super(TasksHomeFormView, self).get_context_data(**kwargs)
        ctx['tasks'] = Task.objects.all().order_by('-created_on')
        ctx['scheduled_tasks'] = ScheduledTask.objects.all().order_by('-created_on')
        return ctx


class LongTaskCreateView(CreateView):
    """
    A class that displays a form to start a long running task.

    """
    template_name = 'long_tasks.html'
    model = LongTask
    fields = ('name', 'duration', )

    def get_context_data(self, **kwargs):
        ctx = super(LongTaskCreateView, self).get_context_data(**kwargs)
        ctx['tasks'] = LongTask.objects.all().order_by('-created_on')
        redis_conn = django_rq.get_connection('default')
        ctx['queue'] = Queue(settings.DJANGO_TEST_RQ_LOW_QUEUE, connection=redis_conn)
        
        return ctx
        
    def form_valid(self, form, ):
        redis_conn = django_rq.get_connection('default')
        if len([x for x in Worker.all(connection=redis_conn) if settings.DJANGO_TEST_RQ_LOW_QUEUE in x.queue_names()]) == 0:
            messages.add_message(self.request, messages.ERROR, 'No active workers for queue!')
            return HttpResponseRedirect(reverse('long_tasks'))
            
        form.instance.result = 'QUEUED'
        long_task = form.save()
        long_runnig_task.delay(long_task)
        messages.info(self.request, 'Long task started.')
        return HttpResponseRedirect(reverse('long_tasks'))


class JobTemplateView(TemplateView):
    """
    A simple template view that gets a job id as a kwarg parameter
    and tries to fetch that job from RQ. It will then print all attributes
    of that object using __dict__.
    """
    template_name = 'job.html'

    def get_context_data(self, **kwargs):
        ctx = super(JobTemplateView, self).get_context_data(**kwargs)
        redis_conn = django_rq.get_connection('default')
        try:
            job = Job.fetch(self.kwargs['job'], connection=redis_conn)
            job = job.__dict__
        except:
            job = None

        ctx['job'] = job
        return ctx
