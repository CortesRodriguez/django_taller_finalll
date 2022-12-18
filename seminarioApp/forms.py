from dataclasses import fields
from django import forms
from seminarioApp.models import Inscrito

class FormReserva(forms.ModelForm):
    class Meta:
        model = Inscrito
        fields = '__all__'