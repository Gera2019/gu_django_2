from django.contrib import admin
from mainapp.models import ProductsCategory, Product

# Register your models here.


admin.site.register(ProductsCategory)
admin.site.register(Product, verbose_name='Продукт')