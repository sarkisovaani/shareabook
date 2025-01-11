from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index ),
    path('add.html', views.add ),
    path('exchange.html', views.exchange ),
    path('search.html', views.search ),
    path('favicon.ico', views.serve_favicon ),
]