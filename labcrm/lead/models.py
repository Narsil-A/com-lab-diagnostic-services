from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

from labservice.models import DiagnosticService


class Lead(models.Model):
    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'

    CHOICES_PRIORITY = (
        (LOW, 'low'),
        (MEDIUM, 'medium'),
        (HIGH, 'high'),
    )

    NEW = 'new'
    CONTACTED = 'contacted'
    WON = 'won'
    LOST = 'lost'

    CHOICES_STATUS = (
        (NEW, 'new'),
        (CONTACTED, 'contacted'),
        (WON, 'won'),
        (LOST, 'lost'),
    )
    
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    description = models.TextField(blank=True, null=True)
    selected_diagnostics = models.ForeignKey(DiagnosticService, related_name='leads',  null=True, blank=True, on_delete=models.SET_NULL)
    priority = models.CharField(max_length=10, choices=CHOICES_PRIORITY, default=MEDIUM)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=NEW)
    converted_to_client = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='leads', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_by',)

    def __str__(self):
        return self.name