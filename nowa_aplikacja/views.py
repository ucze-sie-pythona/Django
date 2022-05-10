from django.shortcuts import render, get_object_or_404, redirect
from .models import Roslina, Nazwa_lac
from .forms import FormularzRoslina, Nazwa_lac_form #importowanie z pliku forms.py
#import login_required()
from django.contrib.auth.decorators import login_required


def nowa_stona(request):
    wszystkie_rosliny = Roslina.objects.all() #wszytskie obiekty utworzone w Django Administrations będą przypisane do tej zmiennej
    return render(request, "nowy_szablon.html", {"dodatkowa_tresc":wszystkie_rosliny}) #przekazywanie do template

@login_required()
def formularz(request):
    form = FormularzRoslina(request.POST or None, request.FILES or None) #przekazujemy klasę utworzone w pliku forms.py
    form_nazwa = Nazwa_lac_form(request.POST or None)
    if all((form.is_valid(), form_nazwa.is_valid())):
        zmienna = form.save(commit=False)
        zmienna2 = form_nazwa.save
        Roslina.dodatkowe_info = zmienna2
        zmienna.save()
        return redirect(nowa_stona)
    return render(request, "szablon_form.html", {'form':form,  'form_nazwa':form_nazwa})

@login_required()
def edytuj(request, id):
    #pierwszy sposób wybrania obiektu do edycji
    # edycja_rosliny = Roslina.objects.get(id)

    #drugi sposób
    edycja_rosliny = get_object_or_404(Roslina,pk=id)
    try:
        edycja_nazwa = Nazwa_lac.objects.get(roslina=edycja_rosliny.id)
    except Nazwa_lac.DoesNotExist:
        edycja_nazwa = None


    #kopiujemy metodę formularz + dodatkowy atgument instance
    form = FormularzRoslina(request.POST or None, request.FILES or None, instance=edycja_rosliny)
    #dodatkowa nazwa łacinska
    form_nazwa = Nazwa_lac_form(request.POST or None, instance=edycja_nazwa)

    if all((form.is_valid(), form_nazwa.is_valid())):
        zmienna = form.save(commit=False)
        zmienna2 = form_nazwa.save
        Roslina.dodatkowe_info = zmienna2
        zmienna.save()
        return redirect(nowa_stona)

    return render(request, "szablon_form.html", {'form': form, 'form_nazwa':form_nazwa})


@login_required()
def usun(request, id):
    usun_rosline = get_object_or_404(Roslina,pk=id)

    if request.method == 'POST':
        usun_rosline.delete()
        return redirect(nowa_stona)

    return render(request, "potwierdz.html", {'roslina': usun_rosline})