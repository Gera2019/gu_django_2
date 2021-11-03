from django.urls import path
from .views import contacts

app_name = 'contactsapp'

urlpatterns = [
    path('', contacts, name = 'main'),
]