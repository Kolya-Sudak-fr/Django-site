# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class YogaClass(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()

class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=128)

class Student(models.Model):
    name = models.CharField(max_length=200)
    enrolled_classes = models.ManyToManyField(YogaClass, related_name='students')
    USERNAME_FIELD = 'id'
    

class Teacher(models.Model):
    name = models.CharField(max_length=200)
    classes = models.ForeignKey(YogaClass, on_delete=models.CASCADE, related_name='teacher')
    USERNAME_FIELD = 'id'