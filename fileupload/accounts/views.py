from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ProfileForm
from .models import Profile

def uploade_profile(request):
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile picture uploaded successfully.')
            return redirect('view_profile')
        else:
            messages.error(request, 'Error uploading profile picture. Please try again.')
    else:
        form = ProfileForm()

    return render(request, 'accounts/uploade_profile.html', {'form': form})

def view_profile(request):
    
    profiles = Profile.objects.all()
    return render(request, 'accounts/view_profile.html', {'profiles': profiles})
