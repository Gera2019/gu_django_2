from django.shortcuts import render
from contactsapp.models import Contact

# Create your views here.

def contacts(request):
    title = 'Контакты'
    contacts = Contact.objects.all()

    context = {'title': title, 'contacts': contacts}
    return render(request, 'contactsapp/contact.html', context)