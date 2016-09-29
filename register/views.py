from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from register.serializers import LogSerializer
from users.serializers import CardSerializer
from users.models import Card
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
import logging

logger = logging.getLogger(__name__)


@csrf_exempt
@api_view(['GET'])
def validate(_, pk):
    card = get_object_or_404(Card, pk=pk)
    card_serializer = CardSerializer(card)
    return JsonResponse(card_serializer.data, status=200)


@csrf_exempt
@api_view(['POST'])
def register(request):
    log_serializer = LogSerializer(data=request.data)
    if log_serializer.is_valid():
        logger.debug(log_serializer)
        log_serializer.save()

        return JsonResponse(log_serializer.data, status=201)
    return JsonResponse(log_serializer.errors, status=400)
