from .models import Komentaras
from django import forms


class KomentarasForm(forms.ModelForm):
    class Meta:
        model = Komentaras
        fields = ('irasas', 'autorius', 'tekstas')
        widgets = {'irasas': forms.HiddenInput(), 'autorius': forms.HiddenInput()}
