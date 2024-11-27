from django.urls import path
from Lenovo.views import *
urlpatterns=[
    path('Options/',Options,name='Options'),
    path('Battery/',Battery,name='Battery'),
]