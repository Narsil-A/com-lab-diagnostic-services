from django import forms 

from .models import DiagnosticService

class AddDiagnosticServiceForm(forms.ModelForm):
    class Meta:
        model = DiagnosticService
        fields = ('name', 'description', 'cost', 'duration',)