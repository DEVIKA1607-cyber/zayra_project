from django.shortcuts import render

def review_list(request):
    return render(request, 'prod_content/prod_details.html')
def track_list(request):
    return render(request, 'prod_content/product_tracking.html')
