from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')

def no_permission(request):
    return render(request, 'no_permission.html')

def features(request):
    return render(request, 'features.html')

def pricing(request):
    return render(request, 'pricing.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')