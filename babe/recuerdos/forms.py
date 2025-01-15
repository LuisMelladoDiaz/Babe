from django import forms
from .models import Recuerdo, ArchivoRecuerdo

class RecuerdoForm(forms.ModelForm):
    class Meta:
        model = Recuerdo
        fields = ['titulo', 'descripcion', 'fecha']

class ArchivoRecuerdoForm(forms.ModelForm):
    class Meta:
        model = ArchivoRecuerdo
        fields = ['archivo', 'tipo']

ArchivoRecuerdoFormSet = forms.inlineformset_factory(
    Recuerdo, ArchivoRecuerdo, form=ArchivoRecuerdoForm, extra=1, can_delete=True
)
