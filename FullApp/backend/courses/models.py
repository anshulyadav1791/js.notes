from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=15, null=True, blank=True, help_text="Enter a Course Name.")
    price = models.FloatField(default=0.0, help_text="Choose your course price.")
    description = models.TextField(null=True, blank=True)
