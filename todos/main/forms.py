from django import forms
from main.models import Todo
from datetime import date

class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = "__all__"

    def clean_title(self):
        title = self.cleaned_data['title']
        words = title.split(' ')
        if len(words) > 5:
            raise forms.ValidationError('Title must be less than or equal to five')
        return title

    def clean_due_date(self):
        due_date = self.cleaned_data['due_date']
        if due_date < date.today():
            raise forms.ValidationError('due date must not be in the past')
        return due_date
