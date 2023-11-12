
from django import forms

from .models import DiagnosticService


class DiagnosticServiceForm(forms.ModelForm):
    class Meta:
        model = DiagnosticService
        fields = '__all__'


