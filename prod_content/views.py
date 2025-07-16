from django.shortcuts import render

def review_list(request):
    return render(request, 'prod_content/review_list.html')
