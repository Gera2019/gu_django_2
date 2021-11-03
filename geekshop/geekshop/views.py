from django.shortcuts import render
from basketapp.models import Basket
from mainapp.models import Product
from contactsapp.models import Contact

def main(request):
    title = 'Магазин'
    basket = []
    products = Product.objects.all()
    contacts = Contact.objects.all()

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    context = {
        'title': title,
        'products': products,
        'contacts': contacts,
        'basket': basket,
    }
    return render(request, 'geekshop/index.html', context)

