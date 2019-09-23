from django import forms
from django.forms import widgets
from webapp.models import choices_list

class TaskForm(forms.Form):
    descr = forms.CharField(max_length=100, required=True, label='Description')
    status = forms.ChoiceField(choices=choices_list, required=False, label='Status')
    completion_date = forms.DateField(required=False, label='Date', widget=widgets.SelectDateWidget)
    full_description = forms.CharField(max_length=3000, required=True, label='Full Description',
                           widget=widgets.Textarea)