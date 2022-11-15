from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    text = "Deneme"
    return HttpResponse("You're looking at question %s." % text)
