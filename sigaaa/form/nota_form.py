from django import forms
from sigaaa.models import Nota

class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(NotaForm, self).__init__(*args, **kwargs)
        for new_field in self.visible_fields():
            new_field.field.widget.attrs['class'] = 'form-control'