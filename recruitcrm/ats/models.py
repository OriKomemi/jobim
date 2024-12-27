from django.db import models

class Recruiter(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, null=True, blank=True)
    company = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class Candidate(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    linked_in = models.URLField(max_length=200, null=True, blank=True)
    experience_years = models.PositiveIntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)  # Indicates if they are actively looking for jobs
    applied_date = models.DateField(auto_now_add=True)  # Automatically sets to now when created

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    job_type = models.CharField(
        max_length=20,
        choices=[('FT', 'Full-Time'), ('PT', 'Part-Time'), ('CT', 'Contract')],
        default='FT',
    )
    location = models.CharField(max_length=100)
    salary_range = models.CharField(max_length=50, null=True, blank=True)
    posted_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE, related_name='jobs', null=True, blank=True) #change multiple

    def __str__(self):
        return self.title

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

class Skill(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class CandidateSkill(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='candidate_skills')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.candidate} -> {self.skill}"

class JobSkill(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='job_skills')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.job} -> {self.skill}"

class Interview(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='interviews')
    scheduled_date = models.DateTimeField()
    interviewer = models.CharField(max_length=100)
    feedback = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Interview for {self.application} on {self.scheduled_date}"