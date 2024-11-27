from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Storage(request):
    return HttpResponse('<h1>Working is Good</h1>')
def Battery(request):
    return HttpResponse('<h1>Long Battery Life</h1>')