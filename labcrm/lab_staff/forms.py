from django import forms 

from .models import LabStaff

class AddLabStaff(forms.ModelForm):
    class Meta:
        model = LabStaff
        fields = ('name', 'email', 'position', 'phone_number','start_date','profession', 'degrees',)