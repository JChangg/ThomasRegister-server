from __future__ import unicode_literals

from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from django.utils import timezone

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Log(models.Model):
    time = models.DateTimeField('time swiped')
    card = models.ForeignKey('users.Card', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.time.strftime("%a %d %b %Y, %H:%M")

    def save(self, *args, **kwargs):
        if not self.time:
            self.time = timezone.now()
        super(Log, self).save(*args, **kwargs)

    class Meta:
        ordering = ('time', )
