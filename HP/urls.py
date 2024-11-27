from django.urls import path
from HP.views import *
urlpatterns=[
    path('Options/',Options,name='Options'),
    path('Battery/',Battery,name='Battery'),
]