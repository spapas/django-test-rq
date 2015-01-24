from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from forms import TaskForm
from tasks import work
from models import Task
from rq.job import Job
import django_rq
import datetime

class TasksHomeFormView(FormView):
    form_class = TaskForm
    template_name = 'tasks_home.html'
    success_url = '/'

    def form_valid(self, form):
        url = form.cleaned_data['url']
        if form.cleaned_data.get('scheduled'):
            scheduler = django_rq.get_scheduler('default')
            job = scheduler.schedule(
                scheduled_time=datetime.datetime.now(),
                func=work,
                args=[url],
                interval=20,
                repeat=100,
            )
        else:
            work.delay(url)
        return super(TasksHomeFormView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super(TasksHomeFormView, self).get_context_data(**kwargs)
        ctx['tasks'] = Task.objects.all()
        return ctx


class JobTemplateView(TemplateView):
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