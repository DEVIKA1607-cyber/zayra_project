from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile

@login_required
def profile_detail(request):
    profile = request.user.profile
    return render(request, 'profiles/profile.html', {'profile': profile})

@login_required
def profile_edit(request):
    profile = request.user.profile
    if request.method == 'POST':
        profile.full_name = request.POST.get('full_name')
        profile.phone = request.POST.get('phone')
        profile.address = request.POST.get('address')
        if 'profile_image' in request.FILES:
            profile.profile_image = request.FILES['profile_image']
        profile.save()
        return redirect('profile_detail') 
    return render(request, 'profiles/edit.html', {'profile': profile})