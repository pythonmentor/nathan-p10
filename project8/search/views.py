from django.shortcuts import render, redirect
from .forms import SearchForm
from offapi.models import Product
from django.views.generic import FormView, ListView

# Create your views here.
class SearchResultsView(ListView):
    model = Product
    template_name = 'search/search.html'
    def get_queryset(self):
        query = self.request.GET.get('q')
        queryset = Product.objects.filter(product_name__icontains=query).values() 
        return queryset[0]['product_id']
        

def search(request):
    query = request.GET.get('q')
    queryset = Product.objects.filter(product_name__icontains=query)[:9]
    context = {'products':queryset, 
                'title': 'Recherche',
                'big_title': 'voici le resultat de votre recherche'
                }

    return render(request, 'search/search.html', context)

def substitute(request, pk):
    product = Product.objects.get(product_id=pk)
    substitute = Product.objects.filter(nutriscore__lt=product.nutriscore) #rajouté en fonction de la category

    context = {'products':substitute, 
                'title': 'Substitue',
                'big_title': 'voici les produits de substitution',
                'previous_product': product,
                'substitut': True
                }

    return render(request, 'search/search.html', context)