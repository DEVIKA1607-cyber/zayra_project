from django.shortcuts import render

def profile_detail(request):
    return render(request, 'profiles/profile_detail.html')

def profile_edit(request):
    return render(request, 'profiles/profile_edit.html')
