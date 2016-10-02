from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.conf import settings 
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token

class Log(models.Model):
    time = models.DateTimeField('time swiped', blank=True)
    card = models.ForeignKey('users.Card', on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        if not self.time:
            self.time = timezone.now()
        super(Log, self).save(*args, **kwargs)

    class Meta:
        ordering = ('time', )


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
