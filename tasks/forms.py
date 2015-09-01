from django import forms


class TaskForm(forms.Form):
    """ A simple form to read a url from the user in order to find out its length
    and either run it asynchronously or schedule it schedule_times times,
    every schedule_interval seconds.
    """
    url = forms.CharField(label='URL', max_length=128, help_text='Enter a url (starting with http/https) to start a job that will download it and count its words' )
    schedule_times = forms.IntegerField(required=False, help_text='How many times to run this job. Leave empty or 0 to run it only once.')
    schedule_interval = forms.IntegerField(required=False, help_text='How much time (in seconds) between runs of the job. Leave empty to run it only once.')

    def clean(self):
        data = super(TaskForm, self).clean()
        schedule_times = data.get('schedule_times')
        schedule_interval = data.get('schedule_interval')

        if schedule_times and not schedule_interval or not schedule_times and schedule_interval:
            msg = 'Please fill both schedule_times and schedule_interval to schedule a job or leave them both empty'
            self.add_error('schedule_times', msg)
            self.add_error('schedule_interval', msg)
