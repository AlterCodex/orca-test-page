from django.contrib import admin
from .models import JobPosting, Skill

# Register your models here.
admin.site.register(JobPosting)
admin.site.register(Skill)