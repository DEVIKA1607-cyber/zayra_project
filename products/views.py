from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def homepage(request):
    categories = Category.objects.all()
    products = Product.objects.order_by('-id')[:8]  # show latest 8
    return render(request, 'products/homepage.html', {
        'categories': categories,
        'products': products
    })

def product_list(request):
    category_id = request.GET.get('category')
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'products/product.html', {'products': products, 'categories': categories})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})
