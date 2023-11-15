from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile
from client.models import Client
from lab_staff.models import LabStaff

class ClientRegistrationForm(UserCreationForm):
    # Add fields from AddClientForm
    name = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=15)

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('name', 'phone_number',)

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            # Assuming UserProfile should be linked with User
            UserProfile.objects.create(
                user=user, 
                role=UserProfile.CLIENT, 
                # Add fields as needed
            )
            # Save client-specific information
            Client.objects.create(
                user=user, 
                name=self.cleaned_data['name'],
                phone_number=self.cleaned_data['phone_number'],
            )
        return user


class LabStaffRegistrationForm(UserCreationForm):

    name = forms.CharField(max_length=100, verbose_name="Full Name")
    phone_number = forms.CharField(max_length=15)
    position = forms.CharField(max_length=100, verbose_name="Position in Lab")
    start_date = forms.DateField(verbose_name="Start Date")
    profession = forms.CharField(max_length=100, verbose_name="Profession")

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('name', 'phone_number', 'position', 'start_date', 'profession')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            # Assuming UserProfile should be linked with User
            UserProfile.objects.create(
                user=user, 
                role=UserProfile.LAB_STAFF, 
                # Add fields as needed
            )
            # Save client-specific information
            LabStaff.objects.create(
                user=user, 
                name=self.cleaned_data['name'],
                phone_number=self.cleaned_data['phone_number'],
                position=self.cleaned_data['position'],
                start_date=self.cleaned_data['start_date'],
                profession=self.cleaned_data['profession']
            )
        return user
