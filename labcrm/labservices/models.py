from django.db import models


class DiagnosticService(models.Model):
    BRUCELLOSIS = 'BRU'
    MYCOBACTERIA_BOVINA = 'MYC'
    LEPTOSPIROSIS = 'LEP'
    RABIA = 'RAB'
    FIEBRE_AFTOSA = 'FIE'

    DIAGNOSTIC_CHOICES = [
        (BRUCELLOSIS, 'Brucellosis'),
        (MYCOBACTERIA_BOVINA, 'Mycobacteria Bovina'),
        (LEPTOSPIROSIS, 'Leptospirosis'),
        (RABIA, 'Rabia'),
        (FIEBRE_AFTOSA, 'Fiebre Aftosa'),
    ]
    name = models.CharField(max_length=3, choices=DIAGNOSTIC_CHOICES)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField(help_text="Duration in minutes")

    def __str__(self):
        return self.get_name_display()
