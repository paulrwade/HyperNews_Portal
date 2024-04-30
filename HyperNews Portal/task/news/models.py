from django.db import models


class News(models.Model):
    created = models.DateTimeField(null=True, blank=True)
    text =  models.CharField(max_length=300)
    title = models.CharField(max_length=128)
    link = models.IntegerField(default=0)

    class META:
        ordering = ['created']

    def __str__(self, *args, **kwargs):
        return f'{self.title}, {self.created}, {self.text}, {self.link}'
