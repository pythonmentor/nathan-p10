from django.shortcuts import render
from .forms import SearchForm
from offapi.models import Product
from django.views.generic import FormView, ListView

# Create your views here.
class SearchResultsView(ListView):
    model = Product
    template_name = 'search/search.html'
    def get_queryset(self):
        query = self.request.GET.get('q')
        queryset = Product.objects.filter(product_name__icontains=query)
        return queryset