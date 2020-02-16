from django.shortcuts import render, redirect
from .forms import SearchForm
from offapi.models import Product, Category
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
    context = {'products': queryset,
               'title': 'Recherche',
               'big_title': 'voici le resultat de votre recherche'}

    return render(request, 'search/search.html', context)


def substitute(request, pk):
    product = Product.objects.get(product_id=pk)
    cat = product.category_id.values_list('id', flat=True)
    print(cat)
    substitute = Product.objects.all().filter(nutriscore__lt=product.nutriscore, category_id__in=cat)  # rajouté en fonction de la category

    context = {'products': substitute,
               'title': 'Substitue',
               'big_title': 'Vous pouvez remplacer cet aliment par:',
               'previous_product': product,
               'substitut': True}

    return render(request, 'search/search.html', context)
