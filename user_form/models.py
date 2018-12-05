from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)

class Skills(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)

class Form(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    skills = models.ForeignKey(Skills, on_delete=models.SET_NULL, null=True)
    income = models.BigIntegerField(default=0)
    edu_qualification = models.CharField(max_length=100)