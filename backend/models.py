from django.db import models
from django.db.models.fields import TextField
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    full_text = TextField()
    date = models.DateTimeField()
    image = models.ImageField(upload_to = 'assets/img/', default = "assets/img/default.jpg")
    autor = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)


    def __str__(self):
        return self.slug


class Lead(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    full_text = TextField()
    date = models.DateTimeField()
    image = models.ImageField(upload_to = 'assets/img/', default = "assets/img/default.jpg")
    autor = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)


    def __str__(self):
        return self.slug
