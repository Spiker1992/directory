from django.db import models

class Listings(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    