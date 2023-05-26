from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('filmes/', views.filmes, name='filmes'),
    path('animes/', views.animes, name='animes'),
]