from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=20)
    year = models.CharField(max_length=10)
    primary_actor = models.CharField(max_length=200)
    secondary_actor = models.CharField(max_length=200)
    producer = models.CharField(max_length=100)
    rate = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    message = models.TextField()
    img_url = models.CharField(max_length=999)

    def __str__(self):
        return self.title


class Series(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=20)
    year = models.CharField(max_length=10)
    seasons = models.CharField(max_length=10)
    actor = models.CharField(max_length=200)
    producer = models.CharField(max_length=100)
    rate = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    message = models.TextField()
    img_url = models.CharField(max_length=999)

    def __str__(self):
        return self.title
