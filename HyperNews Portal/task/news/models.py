from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse


class News(models.Model):
    created = models.DateTimeField(null=True, blank=True)
    text = models.TextField()
    title = models.CharField(max_length=128)
    link = models.IntegerField(default=0)

    class Meta:
        ordering = ['title', 'created']

    def __str__(self, *args, **kwargs):
        return f'{self.title}, {self.created}, {self.text}, {self.link}'
