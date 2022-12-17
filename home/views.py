from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from home.models import Settings


def index(request):
    settings = Settings.objects.get(pk=1)
    context = {'settings':settings}
    return render(request, 'index.html', context)
