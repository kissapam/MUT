from django.urls import path
from . import views

app_name = 'raktar'

urlpatterns = [
    # Login - ez lesz a kezdőoldal
    path('login/', views.login_view, name='login'),
    
    # Dashboard - csak bejelentkezés után
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),

    # Mértékegység
    path('mertekegyseg/', views.mertekegyseg, name='mertekegyseg'),
    path('mertekegyseg/add/', views.addMertekegyseg, name='addMertekegyseg'),
    path('mertekegyseg/delete/<int:id>/', views.deleteMertekegysegById, name='deleteMertekegysegById'),

    # Alkatrészcsoport
    path('alkatreszcsoport/', views.alkatreszcsoport, name='alkatreszcsoport'),
    path('alkatreszcsoport/add/', views.addAlkatreszCsoport, name='addAlkatreszCsoport'),
    path('alkatreszcsoport/delete/<int:id>/', views.deleteAlkatreszCsoportById, name='deleteAlkatreszCsoportById'),

    # Beszállítók
    path('beszallito/', views.beszallito, name='beszallito'),
    path('beszallito/add/', views.addBeszallito, name='addBeszallito'),
    path('beszallito/delete/<int:id>/', views.deleteBeszallitoById, name='deleteBeszallitoById'),

    # Rendszám
    path('rendszam/', views.rendszam, name='rendszam'),
    path('rendszam/add/', views.addRendszam, name='addRendszam'),
    path('rendszam/delete/<int:id>/', views.deleteRendszamById, name='deleteRendszamById'),

    # Alkatrész
    path('alkatresz/', views.alkatresz, name='alkatresz'),
    path('alkatresz/add/', views.addAlkatresz, name='addAlkatresz'),
    path('alkatresz/delete/<int:alkatreszId>/', views.deleteAlkatreszById, name='deleteAlkatreszById'),
    path('alkatresz/delete-by-cikkszam/', views.deleteAlkatreszByCikkszam, name='deleteAlkatreszByCikkszam'),
    path('alkatresz/edit/<int:alkatreszId>/', views.editAlkatreszById, name='editAlkatreszById'),

    # Bevételi bizonylat
    path('bebizonylat/', views.bebizonylat, name='bebizonylat'),
    path('bebizonylat/add/', views.addBebizonylat, name='addBebizonylat'),
    path('bebizonylat/delete/<int:biz_id>/', views.deleteBebizonylat, name='deleteBebizonylat'),
    path('bebizonylat/<int:pk>/', views.beBizonylatsorok, name='beBizonylatsorok'),
    path('bebizonylatsor/add/', views.addBebizonylatsor, name='addBebizonylatsor'),
    # Bevételi bizonylat lezárása
    path('bebizonylat/lezar/<int:biz_id>/', views.lezarBebizonylat, name='lezarBebizonylat'),

    # Kivételi bizonylat
    path('kivbizonylat/', views.kivbizonylat, name='kivbizonylat'),
    path('kivbizonylat/add/', views.addKivbizonylat, name='addKivbizonylat'),
    path('kivbizonylat/delete/<int:biz_id>/', views.deleteKivbizonylat, name='deleteKivbizonylat'),
    path('kivbizonylat/<int:pk>/', views.kivBizonylatsorok, name='kivBizonylatsorok'),
    path('kivbizonylatsor/add/', views.addKivbizonylatsor, name='addKivbizonylatsor'),    
    path('kivbizonylat/lezar/<int:biz_id>/', views.lezarKivbizonylat, name='lezarKivbizonylat'),

    # Leltár
    path('leltar/', views.leltar, name='leltar'),

    # Lezárt bizonylatok
    path('lezart-bizonylatok/', views.lezart_bizonylatok, name='lezart_bizonylatok'),    
    path('bizonylat/megnyit/<int:biz_id>/', views.megnyit_bizonylat, name='megnyit_bizonylat'),

    # Bizonylat exportálás
    path('bizonylat/<int:biz_id>/export/pdf/', views.export_bizonylat_pdf, name='export_bizonylat_pdf'),
    path('bizonylat/<int:biz_id>/export/csv/', views.export_bizonylat_csv, name='export_bizonylat_csv'),
    
   
    
    # Lekérdezések
    path("lekerdezes_ki/", views.lekerdezes_ki, name="lekerdezes_ki"),
    path("lekerdezes_be/", views.lekerdezes_be, name="lekerdezes_be"),
    path("lekerdezes_ossz/", views.lekerdezes_ossz, name="lekerdezes_ossz"),
    
]