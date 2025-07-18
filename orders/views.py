from django.shortcuts import render

def order_list(request):
    return render(request, 'orders/order_list.html')

def order_detail(request, order_id):
    return render(request, 'orders/myorder.html')
