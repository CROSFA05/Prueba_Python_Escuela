from django.forms import ModelForm

from miApp.models import Escuela

class EscuelaForm(ModelForm):
    class Meta:
        model = Escuela
        fields = ["nombre", "siglas"]