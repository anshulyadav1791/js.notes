from django.db import models

class Student(models.Model):   # Capital S
    name = models.CharField(max_length=100)
    age = models.IntegerField()   # Fix here
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name
