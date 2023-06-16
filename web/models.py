from django.db import models


class Message(models.Model):
    text = models.CharField("Mensaje", max_length=200)
    pub_date = models.DateTimeField("date published", auto_now_add=True, blank=True)
    author = models.CharField("Autor", max_length=50, blank=True, null=True)
