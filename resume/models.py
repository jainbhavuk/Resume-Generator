from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=256)
    phone = models.CharField(max_length=10)
    education = models.TextField()
    skills = models.CharField(max_length=256)
    workexperience = models.TextField()
    email = models.EmailField()
    projects = models.TextField(default="")
    achievements = models.TextField(default="")