from rest_framework import serializers
from register.models import Log


class LogSerializer(serializers.ModelSerializer):
    time = serializers.DateTimeField(required=False)

    class Meta:
        model = Log
        fields = ('time', 'card')
