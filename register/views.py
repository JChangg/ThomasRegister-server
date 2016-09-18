from django.shortcuts import render
from django.http import HttpResponse
from models import Log
from users.models import Person


def index(request):
    return HttpResponse("Hello, world. You're at the logging index.")


def log(request, card_id):
    registered_person = Person.objects.get(pk=card_id)
    new_log = Log(person=registered_person)
    new_log.save()
    return HttpResponse("Logged %i: %s" % (card_id, registered_person.username))
