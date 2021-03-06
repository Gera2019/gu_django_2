from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from mainapp.models import ProductsCategory, Product
from basketapp.models import Basket
import random


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []

def get_hot_product():
    products = Product.objects.all()
    return random.sample(list(products), 1)[0]

def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]
    return same_products


def products(request, pk=None, page=1):
    title = 'Каталог'
    links_menu = ProductsCategory.objects.all()
    # basket = get_basket(request.user)
    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)
    products = Product.objects.filter(is_active=True, category__is_active=True).order_by('price')

    if pk is not None:
        if pk == 0:
            category = {'pk': 0, 'name': 'все'}
            products = Product.objects.filter(is_active=True, category__is_active=True).order_by('price')
        else:
            category = get_object_or_404(ProductsCategory, pk=pk)
            products = Product.objects.filter(
                category__pk=pk,
                is_active=True,
                category__is_active=True
            ).order_by('price')

        paginator = Paginator(products, 1)

        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

        context = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products_paginator,
            # 'basket': basket,
        }
        return render(request, 'mainapp/products.html', context )

    context = {
        'title': title,
        'links_menu': links_menu,
        'products': products,
        'hot_product': hot_product,
        'same_products': same_products,
        # 'basket': basket,
    }
    return render(request, 'mainapp/products.html', context)

def product(request, pk):
    title = 'Описание товара'
    links_menu = ProductsCategory.objects.all()
    product = get_object_or_404(Product, pk=pk)
    same_products =  get_same_products(product)
    # basket = get_basket(request.user)

    context = {
        'title': title,
        'links_menu': links_menu,
        'product': product,
        'same_products': same_products,
        # 'basket': basket,
    }
    return render(request, 'mainapp/product.html', context)