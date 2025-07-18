from django.shortcuts import render

def payment_list(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        upi_id = request.POST.get('upi_id')
        return render(request, 'payments/payment_success.html', {
            'amount': amount,
            'upi_id': upi_id
        })
    return render(request, 'payments/payment.html')
def upi_payment(request):
    return render(request, 'payments/upi.html')
