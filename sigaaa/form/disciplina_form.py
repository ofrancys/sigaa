from django import forms
from django.forms import DateInput
from sigaaa.models import Disciplina

class DisciplinaForm(forms.ModelForm):

    class Meta:
        model = Disciplina
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(DisciplinaForm, self).__init__(*args, **kwargs)
        for new_field in self.visible_fields():
            new_field.field.widget.attrs['class'] = 'form-control'
        self.fields['ano'].widget = DateInput(attrs={'type': 'date'})