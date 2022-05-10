from django.urls import path
from nowa_aplikacja.views import nowa_stona,formularz, edytuj, usun

urlpatterns = [
    path('nowa_strona/', nowa_stona, name='strona_glowna'),
    path('formularz/', formularz, name='dodaj'),
    path('edytuj/<int:id>', edytuj, name='edytuj_rosline'),
    path('usun/<int:id>', usun, name='usun_rosline')
]





