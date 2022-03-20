from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

def say_hello(request):
    return render(request,'hello.html',{'name':'Yadigar'})
