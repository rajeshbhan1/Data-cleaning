from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('iata', views.iata, name='iata'),
    path('about', views.about, name='about')
]