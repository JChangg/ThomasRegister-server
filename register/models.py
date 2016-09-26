from __future__ import unicode_literals

from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Log(models.Model):
    time = models.DateTimeField('time swiped', auto_now=True)
    person = models.ForeignKey('users.Person', on_delete=models.CASCADE)

    def __str__(self):
        return self.time.strftime("%a %d %b %Y, %H:%M")

    class Meta:
        ordering = ('time', )
