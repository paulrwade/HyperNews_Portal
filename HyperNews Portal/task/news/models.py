from django.db import models


class News(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    title = models.CharField(max_length=128)
    link = models.IntegerField(default=0)
