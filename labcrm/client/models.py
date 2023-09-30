from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models


class Client(models.Model):
    
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='clients', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name