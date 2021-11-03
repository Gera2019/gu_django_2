from django.contrib import admin
from contactsapp.models import Contact

# Register your models here.
admin.site.register(Contact, verbose_name='Контакты')
