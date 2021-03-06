from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Le compte est créé pour {username}.')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'authentification/register.html', {'form': form})


@login_required(login_url='login')
def profil(request):
    user = request.user
    return render(request, 'authentification/profil.html', {'user': user, 'title': 'Mon profile'})
