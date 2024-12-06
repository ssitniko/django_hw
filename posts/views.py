from django.shortcuts import render
from django.http import HttpResponse



def hello_view(request):
    return HttpResponse('Hello everyuser')

def html_view(request):
    return render(request, 'base.html')