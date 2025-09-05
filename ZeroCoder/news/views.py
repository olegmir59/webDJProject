from django.shortcuts import render


def home(request):
    return render(request, 'news/news.html')

# Create your views here.
