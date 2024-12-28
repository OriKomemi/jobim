from django.db import models
from ats.models.recruiter import Recruiter
from ats.models.skill import Skill
from django.db.models.signals import post_save
from django.core.exceptions import ValidationError
from django.dispatch import receiver




class Candidate(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='candidate_profile')
    phone = models.CharField(max_length=15, null=True, blank=True)
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    experience_years = models.PositiveIntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)  # Actively looking for jobs

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} (Candidate)"

class CandidateSkill(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='candidate_skills')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.candidate} -> {self.skill}"

@receiver(post_save, sender=Candidate)
def candidate_ensure_single_role(sender, instance, **kwargs):
    if Recruiter.objects.filter(user=instance.user).exists():
        raise ValidationError("A user cannot be both a Candidate and a Recruiter.")

@receiver(post_save, sender=Recruiter)
def recruiter_ensure_single_role(sender, instance, **kwargs):
    if Candidate.objects.filter(user=instance.user).exists():
        raise ValidationError("A user cannot be both a Recruiter and a Candidate.")