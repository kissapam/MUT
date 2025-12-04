
from django.urls import path
from . import views

app_name='raktar'

urlpatterns = [
    path('', views.home, name='home'),
    # Mértékegység
    path('mertekegyseg/', views.mertekegyseg, name='mertekegyseg'),
    path('addMertekegyseg/', views.addMertekegyseg, name='addMertekegyseg'), 
    path('deleteMertekegyseg/<int:id>', views.deleteMertekegysegById, name='deleteMertekegysegById'),
    # ALkatrészcsoport
    path('alkatreszcsoport/', views.alkatreszcsoport, name='alkatreszcsoport'),
    path('addAlkatreszCsoport/', views.addAlkatreszCsoport, name='addAlkatreszCsoport'),
    # Rendszám
    path('rendszam/', views.rendszam, name='rendszam'),
    path('addRendszam/', views.addRendszam, name='addRendszam'),
    # Beszállítók
    path('beszallito/', views.beszallito, name='beszallito'),
    path('addBeszallito/', views.addBeszallito, name='addBeszallito'),
    # Alkatrész
    path('alkatresz/', views.alkatresz, name='alkatresz'),    
    path('addAlkatresz/', views.addAlkatresz, name='addAlkatresz'),
    path('deleteAlkatresz/<int:alkatreszId>', views.deleteAlkatreszById, name='deleteAlkatreszById'),
    path('deleteAlkatreszByCikkszam', views.deleteAlkatreszByCikkszam, name='deleteAlkatreszByCikkszam'),
    path('editAlkatresz/<int:alkatreszId>', views.editAlkatreszById, name='editAlkatreszById'),
    # Bevételi
    path("bebizonylat/", views.bebizonylat, name="bebizonylat"),
    path("bebizonylat/add/", views.addBebizonylat, name="addBebizonylat"),
    path("bebizonylat/delete/<int:biz_id>/", views.deleteBebizonylat, name="deleteBebizonylat"),
    # Kivételi
    path("kivbizonylat/", views.kivbizonylat, name="kivbizonylat"),
    path("kivbizonylat/add/", views.addKivbizonylat, name="addKivbizonylat"),
    path("kivbizonylat/delete/<int:biz_id>/", views.deleteKivbizonylat, name="deleteKivbizonylat"),
]