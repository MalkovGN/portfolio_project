from django.db import models


class News(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(blank=True)
    description = models.CharField(max_length=250)

