from django.http import HttpResponse
from models import Log
from users.models import Card
import json
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.query import QuerySet, RawQuerySet
# from django.contrib.auth.decorators import login_required


class QSJSONEncoder(DjangoJSONEncoder):
    """ json.JSONEncoder extension: handle querysets """
    def default(self, obj):
        if isinstance(obj, QuerySet) or isinstance(obj, RawQuerySet):
            return serializers.serialize('python', obj, ensure_ascii=False)
        return super(QSJSONEncoder, self).default(obj)


# @login_required
def authenticate_user(request, id):
    cards = Card.objects.filter(id=id)
    if len(cards) > 0:
        card = cards[0]
        person = card.person
        log = Log(person=person)
        log.save()
        log.refresh_from_db()
        data = {
            'cardID': card.id,
            'time': log.time,
            'name': person.get_name(),
            'groups': person.groups.all(),
            'class': person.class_group,
        }
    else:
        data = {}
    return HttpResponse(json.dumps(data, cls=QSJSONEncoder),
                        content_type="application/json")
