from django.shortcuts import render

# Create your views here.

def shop (request):
    return render (request,"shop.html")

def headerfooter(request):
    return render (request,"headerfooter.html")

