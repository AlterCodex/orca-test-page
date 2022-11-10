from ckeditor.fields import RichTextField
from django.db import models
from django.db.models import TextField


class Skill(models.Model):
    skill = models.CharField(max_length=32)

    class Meta:
        ordering=['skill']

    def __str__(self):
        return self.skill


class JobPosting(models.Model):
    tittle = TextField(default="")
    description = RichTextField(null=True)
    summary = TextField(default="")
    skills = models.ManyToManyField(Skill)





