from django import forms 

from .models import Lead, DiagnosticService

class AddLeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ('name', 'email', 'description', 'phone_number', 'selected_diagnostics', 'priority', 'status',)