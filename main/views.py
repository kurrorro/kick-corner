from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core import serializers
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render
from main.models import Product
from main.forms import ProductForm
import datetime

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  # default 'all'

    if filter_type == "all":
        products = Product.objects.all()
    else:
        products = Product.objects.filter(user=request.user)
        
    context = {
        'shop': 'Kick Corner',
        'npm': '2406437331',
        'name': 'Keisha Vania Laurent',
        'class': 'PBP B',
        'products': products, 
        'last_login': request.COOKIES.get('last_login', 'Never'),
    }

    return render(request, "main.html", context)

def add_product(request): # menghasilkan form yang dapat menambahkan data Product secara otomatis ketika data di-submit dari form
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "add_product.html", context)

@login_required(login_url='/login')
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
    
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

    else:
       form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response