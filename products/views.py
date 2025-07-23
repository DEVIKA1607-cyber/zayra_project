from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from cart.models import WishlistItem
from accounts.decorators import role_required
from orders.models import OrderItem
from .forms import ProductForm
from django.shortcuts import redirect

def homepage(request):
    categories = Category.objects.all()
    products = Product.objects.order_by('-id')[:8] 
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

def category_view(request):
    categories = Category.objects.all()
    return render(request, 'products/categories.html', {'categories': categories})



@role_required('vendor')
def vendor_dashboard(request):
    vendor = request.user
    products = Product.objects.filter(vendor=vendor)  
    order_items = OrderItem.objects.filter(product__vendor=vendor)
    total_orders = order_items.values('order').distinct().count()
    total_earnings = sum(item.price * item.quantity for item in order_items if item.order.status == 'completed')

    context = {
        'products': products,
        'total_earnings': total_earnings,
        'total_products': products.count(),
        'total_orders': total_orders,
    }
    return render(request, 'products/vendor_dashboard.html', context)
@role_required('vendor')
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.vendor = request.user  # Automatically assign logged-in vendor
            product.save()
            return redirect('products:vendor_dashboard')  # Redirect to vendor dashboard
    else:
        form = ProductForm()
    return render(request, 'products/add_product.html', {'form': form})