from django.shortcuts import render
from offapi.models import Product

def home(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    f = Product.objects.values()
    f = list(f)
    return render(request, 'base.html', {'context':f})
