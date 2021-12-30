from django.db import models


class Text(models.Model):
    text = models.TextField(max_length=1000)
    lang = models.CharField(max_length=10)
