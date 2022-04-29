from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nowa_aplikacja/', include('nowa_aplikacja.urls'))
]





