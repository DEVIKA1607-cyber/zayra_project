from django.shortcuts import render, redirect

def payment_view(request):
    return render(request, 'payments/payment.html')  

def upi_view(request):
    if request.method == 'POST':
        return render(request, 'payments/upi.html')
    return redirect('payment')

def order_success_view(request):
    if request.method == 'POST':
        return render(request, 'payments/success.html')
    return redirect('upi_page')
