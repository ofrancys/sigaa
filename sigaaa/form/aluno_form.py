from django import forms
from django.forms import TextInput
from sigaaa.models import Aluno

class AlunoForm(forms.ModelForm):

    class Meta:
        model = Aluno
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AlunoForm, self).__init__(*args, **kwargs)
        for new_field in self.visible_fields():
            new_field.field.widget.attrs['class'] = 'form-control'