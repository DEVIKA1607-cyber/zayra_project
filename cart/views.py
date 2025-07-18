from django.shortcuts import render

def cart_detail(request):
    return render(request, 'cart/cart.html')
def wishlist(request):
    return render(request,'cart/wishlist.html')