# Create your models here.
from django.db import models


class Beszallito(models.Model):
    beszallito = models.CharField(max_length=50)
    lezart = models.BooleanField(default=False)

    def __str__(self):
        return self.beszallito


class Rendszam(models.Model):
    rendszam = models.CharField(max_length=20)
    tulajdonos = models.CharField(max_length=50)
    lezart = models.BooleanField(default=False)

    def __str__(self):
        return self.rendszam


class Mertekegyseg(models.Model):
    mertegys = models.CharField(max_length=20)

    def __str__(self):
        return self.mertegys


class Alkatreszcsoport(models.Model):
    alkcsop = models.CharField(max_length=50)

    def __str__(self):
        return self.alkcsop


class Bizonylat(models.Model):
    genbizid = models.CharField(max_length=20)
    szallito = models.ForeignKey(Beszallito, on_delete=models.CASCADE, related_name="bizonylatok")
    rendszam = models.ForeignKey(Rendszam, on_delete=models.CASCADE, related_name="bizonylatok")
    bizonylattipus = models.BooleanField()
    szamlaszam = models.CharField(max_length=50, blank=True, null=True)
    szallitolevelszam = models.CharField(max_length=50, blank=True, null=True)
    datum = models.DateField()
    lezart = models.BooleanField(default=False)

    def __str__(self):
        return self.gebizid


class Alkatresz(models.Model):
    cikkszam = models.CharField(max_length=100, unique=True)
    leiras = models.CharField(max_length=50)
    info = models.CharField(max_length=300, blank=True, null=True)
    mertekegyseg = models.ForeignKey(Mertekegyseg, on_delete=models.PROTECT, related_name="alkatreszek")
    alkatreszcsoport = models.ForeignKey(Alkatreszcsoport, on_delete=models.PROTECT, related_name="alkatreszek")
    keszlet = models.FloatField(default=0)
    listaar = models.IntegerField()

    def __str__(self):
        return self.cikkszam


class Bizonylatsor(models.Model):
    bizonylat = models.ForeignKey(Bizonylat, on_delete=models.CASCADE, related_name="sorok")
    alkatresz = models.ForeignKey(Alkatresz, to_field="cikkszam", on_delete=models.CASCADE, related_name="bizonylatsorok")
    mennyiseg = models.FloatField()
    aktualisar = models.IntegerField()

    class Meta:
        unique_together = ("bizonylat", "alkatresz")

    def __str__(self):
        return f"{self.bizonylat.gebizid} - {self.alkatresz.cikkszam}"
