from django.contrib import admin
from django.urls import path, include
#pliki media
from django.conf import settings
from django.conf.urls.static import static
#logowanie
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nowa_aplikacja/', include('nowa_aplikacja.urls')),
    path('logowanie/', auth_views.LoginView.as_view(), name = 'logowanie'),
    path('wylogowanie/', auth_views.LogoutView.as_view(), name = 'wylogowanie')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





