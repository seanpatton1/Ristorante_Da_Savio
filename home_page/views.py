from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'home_page/index.html')

def about(request):
    return render(request, 'home_page/about.html')

def menu(request):
    return render(request, 'home_page/menu.html')