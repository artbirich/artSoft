from django.db import models


class Author(models.Model):

    name = models.CharField(blank=False, max_length=500)
    email = models.EmailField(blank=False, primary_key=True)


class Post(models.Model):

    add_email = models.CharField(blank=False, max_length=100)
    comment = models.TextField(blank=False)
    issued = models.DateTimeField()


    author = models.ForeignKey('Author', on_delete=models.CASCADE)