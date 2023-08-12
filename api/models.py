from django.db import models


class Book(models.Model):
    isbn = models.CharField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    year_of_publication = models.IntegerField()
    publisher = models.CharField(max_length=255)
    image_url_s = models.CharField(max_length=255)
    image_url_m = models.CharField(max_length=255)
    image_url_l = models.CharField(max_length=255)
