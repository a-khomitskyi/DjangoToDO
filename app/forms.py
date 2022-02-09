from django import forms
from app.models import Task


class DateInput(forms.DateInput):
    input_type = 'date'


class TaskCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TaskCreateForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        self.fields['until'].widget = DateInput()
        self.fields['until'].widget.attrs = {'class': 'form-control datetimepicker-input',
                                             'data-target': '#datetimepicker1'}

    class Meta:
        model = Task
        fields = ('title', 'description', 'priority', 'until',)
