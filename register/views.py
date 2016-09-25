from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from models import Log


def register_list(request):
    qs = Log.objects.all()
    if request.is_ajax():
        return JsonResponse(qs)
    else:
        context = {'title': 'Logs'}
        return render(request, 'logs.html', context=context)
