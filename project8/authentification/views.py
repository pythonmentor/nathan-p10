from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('email')
            messages.success(request, f'Le compte est créé pour {username}.')
            return redirect('home') 
    else:
        form = UserRegisterForm()
    return render(request, 'authentification/register.html', {'form': form})