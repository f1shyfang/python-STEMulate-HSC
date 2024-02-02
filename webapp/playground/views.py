from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# requests ->responses

#request handler
#action


def say_hello(request):
    #return HttpResponse('Hello World')
    x = calculate()
    return render(request, 'hello.html',{'name': x})


def about_us(request):
    return render(request, 'about_us.html')


def calculate():

    x = 1
    y = 2
    return x
#pull data froma  db can be anything