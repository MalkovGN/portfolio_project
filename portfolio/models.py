from django.db import models
import datetime


class Project(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio/images/', blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

