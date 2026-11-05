from django.shortcuts import render

# Create your views here.

def shop (request):
    return render (request,"shop.html")

def contact (request):
    return render (request,"contact.html")


def headerfooter(request):
    return render(request,"headerfooter.html")

def dashboard(request):
    return render(request,"dashboard.html")

def about(request):
    return render(request,"about.html")

def index(request):
    return render(request,"index.html")
