from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('crypto')  # Remplacez 'accueil' par le nom de votre vue d'accueil
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

    return render(request, 'users/profile.html', {'user_profile': user_profile, 'form': form})


@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        logout(request)
        messages.success(request, 'Votre compte a été supprimé avec succès.')
        return redirect('crypto')  # Redirige vers la page d'accueil ou une autre vue après la suppression
    return render(request, 'users/confirm_delete_account.html')


class WebAppLoginView(LoginView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('crypto')  
        return super().get(request, *args, **kwargs)