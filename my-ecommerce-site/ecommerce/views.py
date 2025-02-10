from django.shortcuts import render
from .models import Product, Category  # 'cart' kaldırıldı

def home(request):
    return render(request, 'ecommerce/home.html')

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'ecommerce/product_detail.html', {'product': product})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'ecommerce/product_list.html', {'products': products})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'ecommerce/category_list.html', {'categories': categories})

def category_detail(request, category_id):
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'ecommerce/category_detail.html', {'category': category, 'products': products})

def cart(request):
    # Sepet işlemleri burada olacak
    return render(request, 'ecommerce/cart.html')

def checkout(request):
    # Ödeme işlemleri burada olacak
    return render(request, 'ecommerce/checkout.html')

def shop(request):
    # Shop sayfası için gerekli işlemler
    return render(request, 'ecommerce/shop.html')

def about(request):
    # Hakkında sayfası için gerekli işlemler
    return render(request, 'ecommerce/about.html')

def contact(request):
    # İletişim sayfası için gerekli işlemler
    return render(request, 'ecommerce/contact.html')