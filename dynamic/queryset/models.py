from django.db import models


class Post(models.Model):
    title = models.TextField(max_length=100)
    content = models.TextField()
    catagory = models.CharField(max_length=100, blank=True, null=True)


def __str__(self):
    return self.title
