
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
    path('beszallito/', views.beszallito, name='beszallito'),
    path('addBeszallito/', views.addBeszallito, name='addBeszallito'),
    path('alkatresz/', views.alkatresz, name='alkatresz'),    
    path('addAlkatresz/', views.addAlkatresz, name='addAlkatresz'),
    path('deleteAlkatresz/<int:alkatreszId>', views.deleteAlkatreszById, name='deleteAlkatreszById'),
    path('deleteAlkatreszByCikkszam', views.deleteAlkatreszByCikkszam, name='deleteAlkatreszByCikkszam'),
    path('editAlkatresz/<int:alkatreszId>', views.editAlkatreszById, name='editAlkatreszById'),
    path('bebizonylat/', views.bebizonylat, name='bebizonylat'),
    path('addBebizonylat/', views.addBebizonylat, name='addBebizonylat'),

]