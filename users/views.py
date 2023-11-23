
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Remplacez 'accueil' par le nom de votre vue d'accueil
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/registration.html', {'form': form})


@login_required
def profile(request):
    user_profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
    else:
        form = ProfileForm(instance=user_profile)

    return render(request, 'profile.html', {'user_profile': user_profile, 'form': form})
