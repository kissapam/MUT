from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Rendszam, Mertekegyseg, Alkatreszcsoport, Alkatresz

def endpoints(request):
    data = {
        "Főoldal az útvonalakkal"               : "/",
        "Mértékegység listázás és hozzáadás"    : "/mertekegyseg",
        "Rendszámok hozzáadása"                 : "/rendszam",    
        "Alkatrészcsoport hozzáadása"           : "/alkatreszcsoport",    
    }
    return JsonResponse(data)


# Create your views here.
def mertekegyseg(request):
    mertekegysegek = Mertekegyseg.objects.all()
    context = {'mertekegysegek': mertekegysegek}
    return render(request,'mertekegyseg.html', context)

def addMertekegyseg(request):
    newMertekegyseg = request.POST["ujMertekegyseg"]
    newRecord = Mertekegyseg(mertegys = newMertekegyseg)
    newRecord.save()
    return redirect("/mertekegyseg")        
##############################################################
def alkatreszcsoport(request):
    alkatreszcsoportok = Alkatreszcsoport.objects.all()
    context = {'alkatreszcsoportok': alkatreszcsoportok}
    return render(request,'alkatreszcsoport.html', context)

def addAlkatreszCsoport(request):
    newAlkatreszCsoport = request.POST["ujAlkatreszCsoport"]
    newRecord = Alkatreszcsoport(alkcsop = newAlkatreszCsoport)
    newRecord.save()
    return redirect("/alkatreszcsoport")   
###############################################################
def rendszam(request):
    rendszamok = Rendszam.objects.all().order_by('rendszam')
    context = {'rendszamok':rendszamok}
    return render(request,'rendszam.html',context)

def addRendszam(request):
    newRendszam = request.POST["ujRendszam"]
    newRekord = Rendszam(rendszam = newRendszam, tulajdonos = "Béla", lezart = False) # Ez így még csak teszt két adat nem az ürlapról jön!
    newRekord.save()
    return redirect("/rendszam")
###############################################################

    