from django.shortcuts import render, redirect
from offapi.models import ProductSaved, Product
from authentification.models import User

# Create your views here.
def add(request):
    return render(request, 'addfav/add.html')

def favorite(request, pk, pk2):
    b = ProductSaved(user_id = User.objects.get(username='admin'),
                    product_id = Product.objects.get(product_id = pk),
                    sub_id = Product.objects.get(product_id = pk2))
    b.save()

    return redirect('/') # doit pouvoir rediriger vers la page d'origine et non la page d'acceuil

def display_favorite(request):
    user = request.user.email #doit pouvoir recevoir le nom de l'utilisateur
    p = ProductSaved.objects.all().filter(user_id= User.objects.get(email=user))
    context = {'products': p,
                'title': 'favorite'
                }   

    return render(request, 'addfav/display.html', context)