from django.shortcuts import render
from offapi.models import Product
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def home(request):
    context = {'products':Product.objects.all(), 
                'title': 'db'
                }

    return render(request, 'blog/db.html', context)

def index(request):
    return render(request, 'blog/index.html')

def base(request):
    return render(request, 'blog/base.html')

def legal(request):
    return render(request, 'blog/legal.html')
