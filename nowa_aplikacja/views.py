from django.shortcuts import render
#importujemy klasę odpowiedzialną za budowanie nowej strony
from django.http import HttpResponse

#definiujemy metodę, którą przekażemy do urls.py
def nowa_stona(request):
    return HttpResponse("To jest nowa zakładka w naszej aplikacji")