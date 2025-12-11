from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
   # Admin
    path('admin/', admin.site.urls),
    
    # Kezdőoldal átirányítása a login oldalra
    path('', RedirectView.as_view(url='/login/', permanent=False)),  # ← Ez itt jó!
    
    # Django beépített auth (login, logout, stb.)
    path('accounts/', include('django.contrib.auth.urls')),
    
    # Raktar alkalmazás URL-jeit include-oljuk namespace-szel
    path('', include('raktar.urls', namespace='raktar')),
]

# Fejlesztéskor (DEBUG=True) a statikus fájlok kiszolgálása
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    if getattr(settings, "MEDIA_URL", None):
        urlpatterns += static(settings.MEDIA_URL, document_root=getattr(settings, "MEDIA_ROOT", None))