from django.urls import path, re_path
from .views import contacts

app_name = 'contactsapp'

urlpatterns = [
    re_path(r'^$', contacts, name = 'main'),
]