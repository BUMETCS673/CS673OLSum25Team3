"""

@ai-generated
Tool: GitHub Copilot
Prompt: N/A
Generated on: 2025-06-08
Modified by: Adriel Domingo
Modifications: changed datetime and status to text
Verified:  reviewed
"""

from django.db import models

class Appointment(models.Model):
    patient_id = models.IntegerField()
    doctor_id = models.IntegerField()
    datetime = models.TextField()
    reason = models.TextField()
    status = models.TextField()

    def __str__(self):
        return f"{self.patient_id} with {self.doctor_id} at {self.datetime}"
    