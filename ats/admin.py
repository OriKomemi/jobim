from django.contrib import admin

from ats.models.application import Application
from ats.models.candidate import Candidate
from ats.models.job import Job

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('candidate', 'job', 'status', 'applied_date', 'updated_date')
    list_filter = ('status', 'applied_date')
    search_fields = ('candidate__first_name', 'candidate__last_name', 'job__title')

admin.site.register(Candidate)
admin.site.register(Job)