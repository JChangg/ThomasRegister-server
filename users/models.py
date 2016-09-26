from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser, Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models


class Person(models.Model):
    username = models.SlugField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    middle_names = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    group = models.ForeignKey(
        Group,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    def save(self, *args, **kwargs):

        if not self.username:
            initials = '%s' % self.first_name[0].lower()
            mn = self.middle_names.split(' ') if self.middle_names else []
            for c in mn:
                initials += c[0].lower()
            initials += (self.last_name[0].lower() if self.last_name else '')
            initials += '_'
            rs = Person.objects.filter(
                username__startswith=initials).order_by('-username')
            if len(rs) != 0:
                num = int(rs[0].username.split('_')[1]) + 1
            else:
                num = 0

            self.username = u"%s%03d" % (initials, num)

        super(Person, self).save(*args, **kwargs)

    def __str__(self):
        return self.username

    @property
    def get_name(self):
        name = self.first_name
        name += (' %s' % self.middle_names if self.middle_names else '')
        name += (' %s' % self.last_name if self.last_name else '')
        return name


class Card(models.Model):
    id = models.IntegerField(primary_key=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return '%i: %s' % (int(self.id), self.person.__str__())


class User(AbstractUser):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.username = self.person.username
        super(User, self).save(*args, **kwargs)
        if self.person.group:
            self.groups.add(self.person.group)
        super(User, self).save(*args, **kwargs)


@receiver(post_save, sender=Person)
def person_post_save(sender, **kwargs):
    person = kwargs.get('instance')
    u = User.objects.filter(person=person)
    if len(u) == 1:
        user = u[0]
        if person.group:
            user.groups.add(person.group)
        user.username = person.username
        user.save()
