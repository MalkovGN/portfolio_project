from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100)
    # url = models.URLField(blank=True)
    date = models.DateField(blank=True)
    description = models.CharField(max_length=250)

