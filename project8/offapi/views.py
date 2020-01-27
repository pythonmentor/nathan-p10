from django.shortcuts import render
from offapi.models import Product
import ast

def home(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    f = Product.objects.values()
    f = list(f)
    return render(request, 'base.html', {'context':f})

def product(request):
    data = Product.objects.get(product_id = 3468570116601)
    nutriments = ast.literal_eval(data.nutriments) 
    context = {'product': data, 
                'title': 'Produit',
                'nutriscore': 'offapi/img/nutriscore-b.svg',
                'sugar': nutriments['sugars_100g'],
                'satured_fat': nutriments['saturated-fat_100g'],
                'fat': nutriments['fat_100g'],
                'salt': nutriments['salt_100g']
                }
    return render(request, 'offapi/product.html', context)