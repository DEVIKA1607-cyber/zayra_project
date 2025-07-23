from django.shortcuts import render
from accounts.decorators import role_required

def delivery_list(request):
    return render(request, 'delivery/delivery_list.html')

@role_required('delivery')
def delivery_dashboard(request):
    return render(request, 'delivery/delivery_dashboard.html')
