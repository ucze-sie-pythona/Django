from django.shortcuts import render
from django.http import HttpResponse
from .models import Roslina

def nowa_stona(request):
    wszystkie_rosliny = Roslina.objects.all() #wszytskie obiekty utworzone w Django Administrations będą przypisane do tej zmiennej
    return render(request, "nowy_szablon.html", {"dodatkowa_tresc":wszystkie_rosliny})