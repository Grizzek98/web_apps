from django.db import models

class Post(models.Model):
    title = models.DateField()
    body = models.TextField()