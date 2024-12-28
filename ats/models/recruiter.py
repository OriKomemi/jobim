from django.db import models

class Recruiter(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, null=True, blank=True)
    company = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
