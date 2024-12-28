from django.db import models

from ats.models.candidate import Candidate
from ats.models.job import Job

class Application(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='applications')
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    cover_letter = models.TextField(null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('AP', 'Applied'),
            ('IN', 'Interviewing'),
            ('OF', 'Offered'),
            ('RE', 'Rejected'),
        ],
        default='AP',
    )
    applied_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.candidate} -> {self.job} ({self.status})"