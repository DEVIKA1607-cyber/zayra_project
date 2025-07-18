from django.shortcuts import render

def order_list(request):
    return render(request, 'orders/user_order.html')

def order_detail(request, order_id):
    return render(request, 'orders/myorder.html')
