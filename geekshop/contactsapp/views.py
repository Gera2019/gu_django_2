from django.shortcuts import render
from contactsapp.models import Contact
from django.conf import settings
from django.core.cache import cache
# Create your views here.
from mainapp.management.commands.fill_db import load_from_json


def contacts(request):
    title = 'Контакты'
    contacts = Contact.objects.all()

    if settings.LOW_CACHE:
        key = f'locations'
        locations = cache.get(key)
        if locations is None:
            locations = load_from_json('contact__locations')
            cache.set(key, locations)
    else:
        locations = load_from_json('contact__locations')

    context = {'title': title, 'contacts': contacts}
    return render(request, 'contactsapp/contact.html', context)