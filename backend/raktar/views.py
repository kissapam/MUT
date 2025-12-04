from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Rendszam, Mertekegyseg, Alkatreszcsoport, Alkatresz, Beszallito, Bizonylat, Bizonylatsor

from .forms import AlkatreszForm
######################################################################## MENU ?????
def home(request):
    return render(request,'home.html')

def mertekegyseg(request):
    mertekegysegek = Mertekegyseg.objects.all()
    context = {'mertekegysegek': mertekegysegek}
    return render(request,'mertekegyseg.html', context)

def addMertekegyseg(request):
    newMertekegyseg = request.POST["ujMertekegyseg"]
    newRecord = Mertekegyseg(mertegys = newMertekegyseg)
    newRecord.save()
    return redirect("/mertekegyseg")

def deleteMertekegysegById(request, id): 
    torlendoMertekegyseg = Mertekegyseg.objects.get(pk = id)
    torlendoMertekegyseg.delete()
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
##############################################################
def beszallito(request):
    beszallitok =Beszallito.objects.all()
    context = {'beszallitok': beszallitok}
    return render(request,'beszallito.html', context)

def addBeszallito(request):
    newBeszallito = request.POST["ujBeszallito"]
    newRecord = Beszallito(beszallito = newBeszallito)
    newRecord.save()
    return redirect("/beszallito")   
###############################################################
def rendszam(request):
    rendszamok = Rendszam.objects.all().order_by('rendszam')
    context = {'rendszamok':rendszamok}
    return render(request,'rendszam.html',context)

def addRendszam(request):
    newRendszam = request.POST["ujRendszam"]
    newTulajdonos = request.POST["ujTulajdonos"]    
    newRekord = Rendszam(rendszam = newRendszam, tulajdonos = newTulajdonos, lezart = False) # Ez így még csak teszt
    newRekord.save()
    return redirect("/rendszam")
###########################################  ALKATRÉSZ 
def alkatresz(request):
    alkatreszek = Alkatresz.objects.all().order_by('cikkszam')
    mertekegysegek = Mertekegyseg.objects.all()
    alkatreszcsoportok = Alkatreszcsoport.objects.all().order_by('alkcsop')
    context = {'alkatreszek':alkatreszek, 'mertekegysegek':mertekegysegek, 'alkatreszcsoportok':alkatreszcsoportok}
    return render(request,'alkatresz.html',context)

def addAlkatresz(request):
    newCikkszam = request.POST["ujCikkszam"]
    newLeiras = request.POST["ujLeiras"]
    newinfo = request.POST["ujInfo"]    
    newMertekegyseg = request.POST["ujMertekegyseg"]
    # kell a mértékegység példány tehát amit az értékadáshoz használok:
    newMertekegysegPeldany = Mertekegyseg.objects.get(mertegys = newMertekegyseg)
    newAlkatreszCsoport = request.POST["ujAlkatreszCsoport"]
    # itt is a példány kell az adatbázisból
    newAlkatreszCsoportPeldany = Alkatreszcsoport.objects.get(alkcsop = newAlkatreszCsoport)
    newKeszlet = request.POST["ujKeszlet"]
    newListaar = request.POST["ujListaar"]
    newRekord = Alkatresz(cikkszam = newCikkszam, leiras = newLeiras, info = newinfo, mertekegyseg = newMertekegysegPeldany, alkatreszcsoport = newAlkatreszCsoportPeldany, keszlet = newKeszlet, listaar = newListaar)
    newRekord.save()
    return redirect("/alkatresz")

def deleteAlkatreszById(request, alkatreszId): # Alkatrész törlése a paraméterben kapott Id alapján
    torlendoAlkatresz = Alkatresz.objects.get(pk = alkatreszId)
    torlendoAlkatresz.delete()
    return redirect("/alkatresz")
    
def deleteAlkatreszByCikkszam(request): # Törlés az alkatrész cikkszáma alapján ürlapon kezdeményezve (nem hiszem hogy marad :) )
    torlendoAlkatreszCikkszam = request.POST["alkatreszCikkszam"]
    torlendoAlkatresz = Alkatresz.objects.get(cikkszam = torlendoAlkatreszCikkszam)
    torlendoAlkatresz.delete()
    return redirect("/alkatresz")

def editAlkatreszById(request, alkatreszId): # ez a rész az AI segítségével készült!!!!
    alkatresz = get_object_or_404(Alkatresz, id=alkatreszId)
    if request.method == "POST":
        form = AlkatreszForm(request.POST, instance=alkatresz)
        if form.is_valid():
            form.save()
            return redirect('/alkatresz')  # vissza a listához
    else:
        form = AlkatreszForm(instance=alkatresz)
    return render(request, 'edit_alkatresz.html', {'form': form})

##############################################   Bevételi Bizonylat

def bebizonylat(request):
    bebizonylatok = Bizonylat.objects.filter(bizonylattipus=True)
    beszallitok = Beszallito.objects.all()
    rendszamok = Rendszam.objects.all()
    context = {
        'bebizonylatok': bebizonylatok,
        'beszallitok': beszallitok,
        'rendszamok': rendszamok
    }
    return render(request, 'bebizonylat.html', context)

def addBebizonylat(request):
    if request.method == "POST":
        newSzallito = request.POST["ujSzallito"]
        newSzallitoPeldany = Beszallito.objects.get(beszallito=newSzallito)
        newSzamlaszam = request.POST["ujSzamlaszam"]
        newSzallitolevelszam = request.POST["ujSzallitolevelszam"]
        newDatum = request.POST["ujDatum"]

        newRekord = Bizonylat(
            genbizid="2555",  # ezt itt még meg kell írnom !!!
            szallito=newSzallitoPeldany,
            bizonylattipus=True,
            szamlaszam=newSzamlaszam,
            szallitolevelszam=newSzallitolevelszam,
            datum=newDatum,
            lezart=False
        )
        newRekord.save()
        return redirect("raktar:bebizonylat")

# Bevételi bizonylat törlése
def deleteBebizonylat(request, biz_id):
    rekord = get_object_or_404(Bizonylat, id=biz_id, bizonylattipus=True)
    rekord.delete()
    return redirect("raktar:bebizonylat")


########################## KIVÉTELI BIZONYLATOK

def kivbizonylat(request):
    kivbizonylatok = Bizonylat.objects.filter(bizonylattipus=False)
    rendszamok = Rendszam.objects.all()
    context = {
        'kivbizonylatok': kivbizonylatok,
        'rendszamok': rendszamok
    }
    return render(request, 'kivbizonylat.html', context)

def addKivbizonylat(request):
    if request.method == "POST":
        newRendszam = request.POST["ujRendszam"]
        newRendszamPeldany = Rendszam.objects.get(rendszam=newRendszam)
        newSzallitolevelszam = request.POST["ujSzallitolevelszam"]
        newDatum = request.POST["ujDatum"]

        newRekord = Bizonylat(
            genbizid="3555",  # ezt MEG KELL ÍRNI MÉG
            rendszam=newRendszamPeldany,
            bizonylattipus=False,
            szallitolevelszam=newSzallitolevelszam,
            datum=newDatum,
            lezart=False
        )
        newRekord.save()
        return redirect("raktar:kivbizonylat")

def deleteKivbizonylat(request, biz_id):
    rekord = get_object_or_404(Bizonylat, id=biz_id, bizonylattipus=False)
    rekord.delete()
    return redirect("raktar:kivbizonylat")
