import json, os
from django.core.management.base import BaseCommand
from authapp.models import ShopUser
from mainapp.models import ProductsCategory, Product
from contactsapp.models import Contact


JSON_PATH = 'mainapp/jsons'

def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), mode='r', encoding='utf8') as infile:
        return json.load(infile)

class Command(BaseCommand):
    def handle(selfself, *args, **options):
        categories = load_from_json('categories')

        ProductsCategory.objects.all().delete()
        for category in categories:
            new_category = ProductsCategory(**category)
            new_category.save()

        products = load_from_json('products')

        Product.objects.all().delete()
        for product in products:
            category_name = product['category']
            _category = ProductsCategory.objects.get(name=category_name)
            product['category'] = _category
            new_product = Product(**product)
            new_product.save()

        contacts = load_from_json('contacts')

        Contact.objects.all().delete()
        for contact in contacts:
            new_contact = Contact(**contact)
            new_contact.save()

        super_user = ShopUser.objects.create_superuser('admin', 'admin@geekshop.local', '123', age=30)
        if super_user:
            print('Super-user created')

