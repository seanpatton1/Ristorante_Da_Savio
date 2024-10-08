from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'home_page/index.html')

def about(request):
    return render(request, 'home_page/about.html')

def menu(request):
    return render(request, 'home_page/menu.html')

def custom_logout_view(request):
    logout(request)  # Logs the user out
    return render(request, 'account/logout.html')