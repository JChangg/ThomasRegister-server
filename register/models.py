from __future__ import unicode_literals

from django.db import models


class Log(models.Model):
    time = models.DateTimeField('time swiped', auto_now=True)
    person = models.ForeignKey('users.Person', on_delete=models.CASCADE)

    def __str__(self):
        return self.time.strftime("%a %d %b %Y, %H:%M")

