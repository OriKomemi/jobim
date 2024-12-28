from django.db import models

from ats.models.skill import Skill

class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)  # City or area
    industry = models.CharField(max_length=100)
    job_function = models.CharField(max_length=100)

    EXPERIENCE_CHOICES = [
        ('internship', 'Internship'),
        ('entry_level', 'Entry level'),
        ('associate', 'Associate'),
        ('mid_senior', 'Mid-Senior level'),
        ('director', 'Director'),
        ('executive', 'Executive'),
    ]
    experience_level = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES)

    JOB_TYPE_CHOICES = [
        ('full_time', 'Full-time'),
        ('part_time', 'Part-time'),
        ('contract', 'Contract'),
        ('temporary', 'Temporary'),
        ('internship', 'Internship'),
        ('other', 'Other'),
    ]
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)

    REMOTE_CHOICES = [
        ('on_site', 'On-site'),
        ('hybrid', 'Hybrid'),
        ('remote', 'Remote'),
    ]
    remote_type = models.CharField(max_length=20, choices=REMOTE_CHOICES)

    has_verifications = models.BooleanField(default=False)  # Indicates if the job listing is verified

    # Metrics
    views = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)  # Replaces posted_date
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} at {self.company}"

    class Meta:
        ordering = ['-created_at']  # Most recent jobs first

class JobSkill(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='job_skills')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.job} -> {self.skill}"