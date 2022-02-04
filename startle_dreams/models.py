from django.db import models

# create a 'Post' object structure in the database.
# basically like creating a table?

class Post(models.Model):
    title = models.DateField()
    body = models.TextField()