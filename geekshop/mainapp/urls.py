from django.urls import path, re_path
from .views import products, product

app_name = 'mainapp'

urlpatterns = [
    re_path(r'^$', products, name = 'main'),
    re_path(r'^product/(?P<pk>\d+)/$', product, name = 'detail'),
    path('category/<int:pk>/page/<int:page>/', products, name='page'),
    path('category/<int:pk>/', products, name='category'),
]
