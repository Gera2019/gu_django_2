"""geekshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from .views import main
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', main, name='main'),
    path('products/', include('mainapp.urls', namespace='products')),
    re_path(r'^contacts/', include('contactsapp.urls', namespace='contacts')),
    re_path(r'^auth/', include('authapp.urls', namespace='auth')),
    re_path(r'^basket/', include('basketapp.urls', namespace='basket')),
    re_path(r'^admin_staff/', include('adminapp.urls', namespace='admin_staff')),
    path('', include('social_django.urls', namespace='social')),
    re_path(r'^orders/', include('ordersapp.urls', namespace='orders')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)