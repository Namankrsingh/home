from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=25)
    roll=models.IntegerField()
    city=models.CharField(max_length=25)
    