from models import Person, Card
from rest_framework import serializers


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('first_name', 'middle_names', 'last_name', 'group', 'username')


class CardSerializer(serializers.ModelSerializer):
    person = PersonSerializer(many=False, read_only=True, required=False)

    class Meta:
        model = Card
        fields = ('id', 'person')
