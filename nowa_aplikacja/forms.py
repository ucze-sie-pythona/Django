from django.forms import ModelForm
from .models import Roslina, Nazwa_lac

class FormularzRoslina (ModelForm):
    class Meta:
        model = Roslina #jako model przekazujemy klasę Roslina
        fields = ['nazwa_rosliny','dni_siewki','obraz',] #podajemy jakie fiels będziemy wyświetlać w formularzu

class Nazwa_lac_form (ModelForm):
    class Meta:
        model = Nazwa_lac
        fields = ['nazwa_lacina']
