from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from labservice.models import DiagnosticService
from django.core.validators import MinLengthValidator

class Client(models.Model):
    
    name = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Client Account")
    email = models.EmailField()
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    description = models.TextField(blank=True, null=True)
    selected_diagnostics = models.ForeignKey(DiagnosticService, related_name='clients',  null=True, blank=True, on_delete=models.SET_NULL)
    created_by = models.ForeignKey(User, related_name='clients', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"
        ordering = ('created_by',)

    def __str__(self):
        return f"{self.name} ({self.selected_diagnostics})"

    name.validators = [MinLengthValidator(2)]