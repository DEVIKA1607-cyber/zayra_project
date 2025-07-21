from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from cart.models import WishlistItem

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
    wishlist_products = WishlistItem.objects.filter(user=request.user).values_list('product_id', flat=True) if request.user.is_authenticated else []
    return render(request, 'products/prod_details.html', {
        'product': product,
        'wishlist_products': wishlist_products,
    })

