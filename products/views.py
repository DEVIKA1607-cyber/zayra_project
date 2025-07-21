from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def homepage(request):
    categories = Category.objects.all()
    products = Product.objects.order_by('-id')[:8]  # show latest 8
    return render(request, 'products/homepage.html', {
        'categories': categories,
        'products': products
    })

def products_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'products/product.html', {
        'selected_category': category,
        'products': products
    })


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/prod_details.html', {'product': product})
