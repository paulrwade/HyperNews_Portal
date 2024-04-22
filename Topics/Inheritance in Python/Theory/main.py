from django.db import models


class Task(models.Model):
    description = models.CharField(max_length=256)
    is_done = models.BooleanField()
    priority = models.IntegerField()


Task.objects.filter(is_done=True).delete()

