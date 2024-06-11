from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def search(request):
    return render(request, 'search.html')
