from django.contrib.auth.models import User
from django.db import models

class Userprofile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)

    LAB_STAFF = 'lab_staff'
    CLIENT = 'client'
    ROLE_CHOICES = [
        (LAB_STAFF, 'Lab Staff'),
        (CLIENT, 'Client'),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=CLIENT)