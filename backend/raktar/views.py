from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Rendszam, Mertekegyseg, Alkatreszcsoport, Alkatresz, Beszallito, Bizonylat, Bizonylatsor, AlapAdat

from .forms import AlkatreszForm
############################################ MENU 
def home(request):
    return render(request,'home.html')
############################################ MÉRTÉKEGYSÉG
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
        
############################################ ALKATRÉSZ
def alkatreszcsoport(request):
    alkatreszcsoportok = Alkatreszcsoport.objects.all()
    context = {'alkatreszcsoportok': alkatreszcsoportok}
    return render(request,'alkatreszcsoport.html', context)

def addAlkatreszCsoport(request):
    newAlkatreszCsoport = request.POST["ujAlkatreszCsoport"]
    newRecord = Alkatreszcsoport(alkcsop = newAlkatreszCsoport)
    newRecord.save()
    return redirect("/alkatreszcsoport")

def deleteAlkatreszCsoportById(request, id): 
    torlendoAlkatreszCsoport = Alkatreszcsoport.objects.get(pk = id)
    torlendoAlkatreszCsoport.delete()
    return redirect("/alkatreszcsoport")          
############################################ BESZÁLLÍTÓ
def beszallito(request):
    beszallitok =Beszallito.objects.all()
    context = {'beszallitok': beszallitok}
    return render(request,'beszallito.html', context)

def addBeszallito(request):
    newBeszallito = request.POST["ujBeszallito"]
    newRecord = Beszallito(beszallito = newBeszallito)
    newRecord.save()
    return redirect("/beszallito")

def deleteBeszallitoById(request, id): 
    torlendoBeszallito = Beszallito.objects.get(pk = id)
    torlendoBeszallito.delete()
    return redirect("/beszallito")             
########################################### RENDSZÁM
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

def deleteRendszamById(request, id): 
    torlendoRendszam = Rendszam.objects.get(pk = id)
    torlendoRendszam.delete()
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

##########################   Bevételi Bizonylat

def bebizonylat(request):    
    bebizonylatok = Bizonylat.objects.filter(bizonylattipus=True)
    beszallitok = Beszallito.objects.all()
    rendszamok = Rendszam.objects.all()
    context = {
        'bebizonylatok': bebizonylatok,
        'beszallitok': beszallitok,
        'rendszamok': rendszamok,
    }
    return render(request, 'bebizonylat.html', context)

def addBebizonylat(request):
    if request.method == "POST":
        newSzallito = request.POST["ujSzallito"]
        newSzallitoPeldany = Beszallito.objects.get(beszallito=newSzallito)
        newSzamlaszam = request.POST["ujSzamlaszam"]
        newSzallitolevelszam = request.POST["ujSzallitolevelszam"]
        newDatum = request.POST["ujDatum"]

        alapadat = AlapAdat.objects.first()
        if not alapadat:
            raise ValueError("Nincs beállítva AlapAdat rekord!")

        # 1. lépés: létrehozás genbizid nélkül
        newRekord = Bizonylat(
            szallito=newSzallitoPeldany,
            bizonylattipus=True,
            szamlaszam=newSzamlaszam,
            szallitolevelszam=newSzallitolevelszam,
            datum=newDatum,
            lezart=False
        )
        newRekord.save()
        # 2. lépés: genbizid kiszámítása
        kulonbseg = newRekord.id - alapadat.maxBizId        
        genbizid =f"BE{alapadat.ev}_{kulonbseg:04d}" # mindig 4 számjegy, nullákkal feltöltve
        newRekord.genbizid = genbizid
        newRekord.save(update_fields=["genbizid"])

        return redirect("raktar:bebizonylat")

def bebizonylatsorok(request, pk):
    aktualis_bizonylat = get_object_or_404(Bizonylat, pk=pk)
    aktualis_alakterszek = Alkatresz.objects.all()
    aktualisbiz_sorai = aktualis_bizonylat.sorok.all()   # a related_name miatt
    osszeg = 0
    for sor in aktualisbiz_sorai:
        osszeg += sor.aktualisar * sor.mennyiseg
    return render(request,"bebizonylatsorok.html",{"alkatreszek":aktualis_alakterszek,"bizonylat": aktualis_bizonylat, "sorok": aktualisbiz_sorai,"osszeg": f"{osszeg:,.0f} ft".replace(",", ".")})
## 
 
def addBebizonylatsor(request):
    newBizonylatId = request.POST["bizonylat_id"]
    newBizonylatPeldany = Bizonylat.objects.get(id=newBizonylatId)
    newAlkatresz = request.POST["ujAlkatresz"]    
    newAlkatreszPeldany = Alkatresz.objects.get(cikkszam=newAlkatresz)
    newMennyiseg = request.POST["ujMennyiseg"]
    newAktualisar = request.POST["ujAktualisar"]    
    newRecord = Bizonylatsor(bizonylat = newBizonylatPeldany, alkatresz =newAlkatreszPeldany, mennyiseg = newMennyiseg, aktualisar = newAktualisar)
    newRecord.save()
    newAlkatreszPeldany.keszlet += float(request.POST["ujMennyiseg"])
    newAlkatreszPeldany.listaar = float(request.POST["ujAktualisar"])
    newAlkatreszPeldany.save()
     
    
    return redirect(request.META.get('HTTP_REFERER')) # ugyanarra az oldalra térek vissza ahonnan jött a request
    
    

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
        newDatum = request.POST["ujDatum"]

        alapadat = AlapAdat.objects.first()
        if not alapadat:
            raise ValueError("Nincs beállítva AlapAdat rekord!")

        newRekord = Bizonylat(            
            rendszam=newRendszamPeldany,
            bizonylattipus=False,
            datum=newDatum,
            lezart=False
        )
        newRekord.save()        
        # 2. lépés: genbizid kiszámítása
        kulonbseg = newRekord.id - alapadat.maxBizId        
        genbizid =f"KI{alapadat.ev}_{kulonbseg:04d}" # mindig 4 számjegy, nullákkal feltöltve
        newRekord.genbizid = genbizid
        newRekord.save(update_fields=["genbizid"])
        return redirect("raktar:kivbizonylat")

def deleteKivbizonylat(request, biz_id):
    rekord = get_object_or_404(Bizonylat, id=biz_id, bizonylattipus=False)
    rekord.delete()
    return redirect("raktar:kivbizonylat")

########################## LEKÉRDEZÉSEK  
def lekerdezes_ki(request):
    rendszamok = Rendszam.objects.all()
    sorok = None
    kivalasztott = None
    kivalasztott_cikk = None

    if request.method == "POST":
        kivalasztott = request.POST.get("keresettRendszam")
        kivalasztott_cikk = request.POST.get("keresettCikkszam")

        # minden kiadási bizonylat listázása:
        sorok = Bizonylatsor.objects.filter(bizonylat__bizonylattipus=False)

        # ha van rendszám → szűrés
        if kivalasztott:
            sorok = sorok.filter(
                bizonylat__rendszam__rendszam=kivalasztott
            )

        # ha van cikkszám részlet → LIKE szűrés
        if kivalasztott_cikk:
            sorok = sorok.filter(
                alkatresz__cikkszam__icontains=kivalasztott_cikk
            )

        sorok = sorok.select_related("bizonylat", "alkatresz") \
                     .order_by("-bizonylat__datum")

    return render(request, 'lekerdezes_ki.html', {
        'rendszamok': rendszamok,
        'sorok': sorok,
        'kivalasztott': kivalasztott,
        'kivalasztott_cikk': kivalasztott_cikk,
    })


def lekerdezes_be(request):
    beszallitok = Beszallito.objects.all()
    sorok = None
    kivalasztott = None
    kivalasztott_cikk = None

    if request.method == "POST":
        kivalasztott = request.POST.get("keresettBeszallito")
        kivalasztott_cikk = request.POST.get("keresettCikkszam")

        # induló queryset: csak BEVÉTELEZETT bizonylatok sorai
        sorok = Bizonylatsor.objects.filter(bizonylat__bizonylattipus=True)
        
        
        # ha van beszállító megadva:
        if kivalasztott:
            sorok = sorok.filter(
                bizonylat__szallito__beszallito=kivalasztott
            )


        # ha van cikkszám részlet → LIKE szűrés
        if kivalasztott_cikk:
            sorok = sorok.filter(
                alkatresz__cikkszam__icontains=kivalasztott_cikk
            )

        # optimalizálás + rendezés
        sorok = (
            sorok
            .select_related("bizonylat", "bizonylat__szallito", "alkatresz")
            .order_by("-bizonylat__datum")
        )

    return render(request, 'lekerdezes_be.html', {
        'beszallitok': beszallitok,
        'sorok': sorok,
        'kivalasztott_cikk': kivalasztott_cikk,
    })

def lekerdezes_ossz(request):
    sorok = None
    keresett_cikk = None

    if request.method == "POST":
        keresett_cikk = request.POST.get("keresettCikkszam")

        # induló queryset: minden bizonylatsor
        sorok = Bizonylatsor.objects.all()
        
        # ha van cikkszám részlet → LIKE szűrés
        if keresett_cikk:
            sorok = sorok.filter(
                alkatresz__cikkszam__icontains=keresett_cikk
            )

        # optimalizálás + rendezés
        sorok = (
            sorok
            .select_related(
                "bizonylat",
                "bizonylat__szallito",
                "bizonylat__rendszam",
                "alkatresz"
            )
            .order_by("-bizonylat__datum")
        )

    return render(request, 'lekerdezes_ossz.html', {
        'sorok': sorok,
        'keresett_cikk': keresett_cikk,
    })
