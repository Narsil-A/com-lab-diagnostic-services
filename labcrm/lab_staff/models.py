from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinLengthValidator

class LabStaff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="LabStaff Account")
    name = models.CharField(max_length=100, verbose_name="Full Name")
    email = models.EmailField()
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    position = models.CharField(max_length=100, verbose_name="Position in Lab")
    start_date = models.DateField(verbose_name="Start Date")
    profession = models.CharField(max_length=100, verbose_name="Profession")
    degrees = models.CharField(max_length=200, verbose_name="Degrees/Certifications")

    class Meta:
        verbose_name = "Lab Staff"
        verbose_name_plural = "Lab Staff"
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.position})"

    name.validators = [MinLengthValidator(2)]

    
