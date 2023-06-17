from django.db import models
from datetime import datetime, timezone


class Message(models.Model):
    text = models.CharField("Mensaje", max_length=200)
    pub_date = models.DateTimeField("date published", auto_now_add=True, blank=True)
    author = models.CharField("Autor", max_length=50, blank=True, null=True)

    @property
    def is_within_a_day(self):
        now = datetime.now(timezone.utc)
        created_at = self.pub_date
        if (now - created_at).total_seconds() <= 24 * 60 * 60:
            return True
        else:
            return False

    @property
    def is_within_a_week(self):
        now = datetime.now(timezone.utc)
        created_at = self.pub_date
        if (now - created_at).days <= 7:
            return True
        else:
            return False