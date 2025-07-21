from django.shortcuts import render

def track_list(request):
    return render(request, 'prod_content/product_tracking.html')
