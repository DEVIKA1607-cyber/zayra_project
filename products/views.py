from django.shortcuts import render

def product_list(request):
    return render(request, 'products/product_list.html')

def product_detail(request, pk):
    return render(request, 'products/product.html')

def homepage(request):
    return render(request, 'products/homepage.html')