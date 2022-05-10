from django.db import models

class Nazwa_lac (models.Model):
    nazwa_lacina = models.CharField(max_length=60, unique=True, blank=True, null=True)
    def __str__(self):
        return self.nazwa_lacina

class Roslina (models.Model):
    nazwa_rosliny = models.CharField(max_length=60, unique=True, blank=True, null=True)
    dni_siewki = models.PositiveSmallIntegerField(blank=True, null=True)
    poziom = (
      ('1','Łatwy'),
      ('2','Średni'),
      ('3','Trudny')
    )
    trudnosc_uprawy = models.CharField(choices=poziom, default='2', max_length=8, blank=True )
    wysokosc = models.PositiveSmallIntegerField(null=True)
    obraz = models.ImageField(upload_to="zdjecia", null=True)
    dodatkowe_info = models.OneToOneField(Nazwa_lac, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nazwa_rosliny




