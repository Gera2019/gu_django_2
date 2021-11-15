from django.urls import path, re_path
from .views import products, product

app_name = 'mainapp'

urlpatterns = [
    re_path(r'^$', products, name = 'main'),
    re_path(r'^category/(?P<pk>\d+)/$', products, name = 'category'),
    re_path(r'^product/(?P<pk>\d+)/$', product, name = 'detail'),
    re_path(r'^category/(?P<pk>\d+)/page/(?P<page>\d+)/$', products, name='page'),
]
