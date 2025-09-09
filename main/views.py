from django.shortcuts import render
from main.models import Product

def show_main(request):
    products = Product.objects.all()  # ambil semua produk
    context = {
        'shop': 'Kick Corner',
        'npm': '2406437331',
        'name': 'Keisha Vania Laurent',
        'class': 'PBP B',
        'products': products, 
    }

    return render(request, "main.html", context)