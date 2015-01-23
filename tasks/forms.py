from django import forms

class TaskForm(forms.Form):
    url = forms.CharField(label='URL', max_length=128)