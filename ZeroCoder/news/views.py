from django.shortcuts import render


def home(request):
    return render(request, 'main/about.html')

# Create your views here.
