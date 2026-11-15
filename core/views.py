from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

# Create your views here.


def contact (request):
    return render (request,"contact.html")


def headerfooter(request):
    return render(request,"headerfooter.html")


def about(request):
    return render(request,"about.html")

def index(request):
    return render(request,"index.html")

def shop(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        name = request.POST.get('name')
        price = request.POST.get('price') or 0

        print("Image:", image)
        print("Name:", name)
        print("Price:", price)

        Product.objects.create(   
            image=image,
            name=name,
            price=price
            )
    queryset = Product.objects.all()
    context = {
        'products': queryset
    }

    return render(request, "shop.html", context)

def dashboard(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        name = request.POST.get('name')
        price = request.POST.get('price') or 0

        print("Image:", image)
        print("Name:", name)
        print("Price:", price)

        Product.objects.create(   
            image=image,
            name=name,
            price=price
            )
    queryset = Product.objects.all()
    context = {
        'products': queryset
    }

    return render(request, "dashboard.html", context)

def delete_product(request, product_id):
        product = get_object_or_404(Product, id=product_id)
        product.delete()
        return redirect('dashboard')


def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        image = request.FILES.get('image')

        product.name = name
        product.price = price

        if image:
            product.image = image

        product.save()

        return redirect('dashboard')

    return render(request, 'update_product.html', {'product': product})

