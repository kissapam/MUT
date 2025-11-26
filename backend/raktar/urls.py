
from django.urls import path
from . import views

app_name='raktar'
urlpatterns = [
    path('',views.endpoints),
    path('mertekegyseg/', views.mertekegyseg, name='mertekegyseg'),
    path('addMertekegyseg/', views.addMertekegyseg, name='addMertekegyseg'), 
    path('alkatreszcsoport/', views.alkatreszcsoport, name='alkatreszcsoport'),
    path('addAlkatreszCsoport/', views.addAlkatreszCsoport, name='addAlkatreszCsoport'),
    path('rendszam/', views.rendszam, name='rendszam'),
    path('addRendszam/', views.addRendszam, name='addRendszam'), 
]
