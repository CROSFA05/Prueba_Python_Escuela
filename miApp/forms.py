from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import Escuela, Maestro

class EscuelaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Guardar', css_class='btn btn-success'))

    class Meta:
        model = Escuela
        fields = ["nombre", "siglas"]

class MaestroForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('nombre', css_class='form-group col-md-4 mb-0'),
                Column('fecha_nacimiento', css_class='form-group col-md-4 mb-0'),
                Column('sexo', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('escuela', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Guardar', css_class='btn btn-success mt-3')
        )
    
    class Meta:
        model = Maestro
        fields = ["nombre", "escuela", "fecha_nacimiento", "sexo"]