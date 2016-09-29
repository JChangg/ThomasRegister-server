from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Log(models.Model):
    time = models.DateTimeField('time swiped', blank=True)
    card = models.ForeignKey('users.Card', on_delete=models.CASCADE, null=True)

    # def __str__(self):
    #     return self.time.strftime("%a %d %b %Y, %H:%M")

    def save(self, *args, **kwargs):
        if not self.time:
            self.time = timezone.now()
        super(Log, self).save(*args, **kwargs)

    class Meta:
        ordering = ('time', )
