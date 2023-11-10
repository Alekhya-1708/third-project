from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def rohit(request):
    return render(request,'mi.html')
def bumbra(request):
    return HttpResponse('<h1>he is a good player</h1>')