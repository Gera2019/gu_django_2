from django.urls import path, re_path
from .views import products, product
from django.views.decorators.cache import cache_page

app_name = 'mainapp'

urlpatterns = [
    path('', products, name = 'main'),
    path('product/<int:pk>/', product, name = 'detail'),
    path('category/<int:pk>/page/<int:page>/', products, name='page'),
    path('category/<int:pk>/', products, name='category'),
    path('category/<int:pk>/page/<int:page>/', products, name='page'),
]
