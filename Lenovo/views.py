from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Options(request):
    return HttpResponse('<h1>Limited Upgrade Options</h1>')
def Battery(request):
    return HttpResponse('<h1>Good Battery Life</h1>')