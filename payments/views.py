from django.shortcuts import render

def payment_list(request):
    return render(request, 'payments/payment_list.html')
