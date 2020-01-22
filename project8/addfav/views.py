from django.shortcuts import render
from offapi.models import ProductSaved, Product
from django.contrib.auth.models import User

# Create your views here.
def add(request):
    return render(request, 'addfav/add.html')

def favorite(request):
    b = ProductSaved(user_id = User.objects.get(username='admin'),
                    product_id = Product.objects.get(product_id = 3174780000431),
                    sub_id = Product.objects.get(product_id = 3068320110097))
    b.save()

    return render(request, 'addfav/add.html')