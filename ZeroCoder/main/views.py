from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

def services(request):
    return render(request, 'main/services.html')


def data(request):
    return HttpResponse("<h1>Это страница DATA</h1>")


def test(request):
    return HttpResponse("<h1>Это страница TEST</h1>")
