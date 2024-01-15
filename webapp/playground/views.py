from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# requests ->responses

#request handler
#action


def say_hello(request):
    return HttpResponse('Hello World')

#pull data froma  db can be anything