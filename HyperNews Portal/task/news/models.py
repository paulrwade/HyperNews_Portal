from django.db import models


class News(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField()
