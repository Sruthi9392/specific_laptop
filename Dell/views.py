from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Quality(request):
    return HttpResponse('<h1>Quality Control Issues</h1>')
def battery(request):
    return HttpResponse('<h1>Good Battery Life</h1>')