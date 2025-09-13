from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render
from main.models import Product
from main.forms import ProductForm

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

def add_product(request): # menghasilkan form yang dapat menambahkan data Product secara otomatis ketika data di-submit dari form
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "add_product.html", context)

def show_product(request, id):
    product = get_object_or_404(Product, pk=id) # untuk mengambil objek News berdasarkan primary key (id). Jika objek tidak ditemukan, akan mengembalikan halaman 404
    product.increment_views() # menambah jumlah views

    context = {
        'product': product
    }
    return render(request, "product_detail.html", context)

def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list) # translate objek model menjadi format lain seperti dalam fungsi ini adalah XML
    return HttpResponse(xml_data, content_type="application/xml") 

def show_json(request):
    product_list = Product.objects.all()
    json_data = serializers.serialize("json", product_list)
    return HttpResponse(json_data, content_type="application/json") # return function berupa HttpResponse yang berisi parameter data hasil query yang sudah diserialisasi menjadi JSON dan parameter

def show_xml_by_id(request, product_id):
    try: 
        product_item = Product.objects.filter(pk=product_id) # ambil sesuai id
        xml_data = serializers.serialize("xml", product_item) # serialisasi jd xml
        return HttpResponse(xml_data, content_type="application/xml") # return HttpResponse yg berisi parameter data hasil query yg sdh diserialisasi
    except Product.DoesNotExist:
       return HttpResponse(status=404)

def show_json_by_id(request, product_id):
    try: 
        news_item = Product.objects.get(pk=product_id) # get terbatas 1 objek
        json_data = serializers.serialize("json", [news_item])
        return HttpResponse(json_data, content_type="application/json")
    except Product.DoesNotExist:
       return HttpResponse(status=404)