from django.contrib import admin
#importowanie klasy Roslina z pliku models.py
from .models import Roslina, Nazwa_lac

# zamiast admin.site.register(Roslina) napiszemy:
@admin.register(Roslina) #@jest to dekorator
class RoslinaAdmin(admin.ModelAdmin):
    list_display = ("nazwa_rosliny","trudnosc_uprawy")
    list_filter = ("trudnosc_uprawy",)
    search_fields = ("nazwa_rosliny",)


admin.site.register(Nazwa_lac)