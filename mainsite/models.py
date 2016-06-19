from django.db import models
from django.utils import timezone
import os


from django import template
register = template.Library()

class Member(models.Model):
    pic = models.ImageField(upload_to='./mainsite/static/')
    username = models.CharField(default="Username", max_length=20)
    password = models.CharField(default="Password" ,max_length=20)
    name = models.CharField(default="Name", max_length=50)
    email = models.EmailField(default="e-mail")
    branch = models.CharField(default="Branch", max_length=50)
    work = models.CharField(default="Company/University", max_length=50)
    DOB = models.DateField(default=timezone.now());
    year = models.CharField(default="Year", max_length=12)
    bio = models.TextField(default="Lorem ipsum sit dolot fuck this shit !")
    linkedin = models.URLField(null=True)
    resume = models.FileField(null=True,upload_to='./mainsite/static')
    active = models.BooleanField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.name

    @property
    def resumeFilename(self,):
        return  os.path.basename(self.resume.name)

    # @property
    def picFilename(self,):
        return  os.path.basename(self.pic.name)


class Project(models.Model):
    pic = models.ImageField(null=True)
    name = models.CharField(default="Name", max_length=50)
    description = models.TextField(default="Shitty Project")
    github = models.URLField(null=True)
    completed = models.BooleanField()

    def __str__(self):
        return self.name

    def publish(self):
        self.save()
