from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Rendszam, Mertekegyseg, Alkatreszcsoport, Alkatresz, Beszallito, Bizonylat, Bizonylatsor, AlapAdat
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import Http404
from .forms import AlkatreszForm

############################################ MENU 
def home(request):
    return render(request,'home.html')

############################################ MÉRTÉKEGYSÉG
@login_required
def mertekegyseg(request):
    mertekegysegek = Mertekegyseg.objects.all()
    context = {'mertekegysegek': mertekegysegek}
    return render(request,'mertekegyseg.html', context)

@login_required
def addMertekegyseg(request):
    if request.method == "POST":
        try:
            newMertekegyseg = request.POST["ujMertekegyseg"]
            newRecord = Mertekegyseg(mertegys=newMertekegyseg)
            newRecord.save()
            messages.success(request, "Mértékegység sikeresen hozzáadva!")
        except Exception as e:
            messages.error(request, f"Hiba történt: {str(e)}")
    return redirect("raktar:mertekegyseg")

@login_required
def deleteMertekegysegById(request, id): 
    try:
        torlendoMertekegyseg = Mertekegyseg.objects.get(pk=id)
        torlendoMertekegyseg.delete()
        messages.success(request, "Mértékegység sikeresen törölve!")
    except Exception as e:
        messages.error(request, f"Hiba történt a törlés során: {str(e)}")
    return redirect("raktar:mertekegyseg")
        
############################################ ALKATRÉSZCSOPORT
@login_required
def alkatreszcsoport(request):
    alkatreszcsoportok = Alkatreszcsoport.objects.all()
    context = {'alkatreszcsoportok': alkatreszcsoportok}
    return render(request,'alkatreszcsoport.html', context)

@login_required
def addAlkatreszCsoport(request):
    if request.method == "POST":
        try:
            newAlkatreszCsoport = request.POST["ujAlkatreszCsoport"]
            newRecord = Alkatreszcsoport(alkcsop=newAlkatreszCsoport)
            newRecord.save()
            messages.success(request, "Alkatrészcsoport sikeresen hozzáadva!")
        except Exception as e:
            messages.error(request, f"Hiba történt: {str(e)}")
    return redirect("raktar:alkatreszcsoport")

@login_required
def deleteAlkatreszCsoportById(request, id): 
    try:
        torlendoAlkatreszCsoport = Alkatreszcsoport.objects.get(pk=id)
        torlendoAlkatreszCsoport.delete()
        messages.success(request, "Alkatrészcsoport sikeresen törölve!")
    except Exception as e:
        messages.error(request, f"Hiba történt a törlés során: {str(e)}")
    return redirect("raktar:alkatreszcsoport")

############################################ BESZÁLLÍTÓ
@login_required
def beszallito(request):
    beszallitok = Beszallito.objects.all()
    context = {'beszallitok': beszallitok}
    return render(request,'beszallito.html', context)

@login_required
def addBeszallito(request):
    if request.method == "POST":
        try:
            newBeszallito = request.POST["ujBeszallito"]
            newRecord = Beszallito(beszallito=newBeszallito)
            newRecord.save()
            messages.success(request, "Beszállító sikeresen hozzáadva!")
        except Exception as e:
            messages.error(request, f"Hiba történt: {str(e)}")
    return redirect("raktar:beszallito")

@login_required
def deleteBeszallitoById(request, id): 
    try:
        torlendoBeszallito = Beszallito.objects.get(pk=id)
        torlendoBeszallito.delete()
        messages.success(request, "Beszállító sikeresen törölve!")
    except Exception as e:
        messages.error(request, f"Hiba történt a törlés során: {str(e)}")
    return redirect("raktar:beszallito")

########################################### RENDSZÁM
@login_required
def rendszam(request):
    rendszamok = Rendszam.objects.all().order_by('rendszam')
    context = {'rendszamok': rendszamok}
    return render(request,'rendszam.html', context)

@login_required
def addRendszam(request):
    if request.method == "POST":
        try:
            newRendszam = request.POST["ujRendszam"]
            newTulajdonos = request.POST["ujTulajdonos"]
            newRekord = Rendszam(rendszam=newRendszam, tulajdonos=newTulajdonos, lezart=False)
            newRekord.save()
            messages.success(request, "Gépjármű sikeresen hozzáadva!")
        except Exception as e:
            messages.error(request, f"Hiba történt: {str(e)}")
    return redirect("raktar:rendszam")

@login_required
def deleteRendszamById(request, id): 
    try:
        torlendoRendszam = Rendszam.objects.get(pk=id)
        torlendoRendszam.delete()
        messages.success(request, "Gépjármű sikeresen törölve!")
    except Exception as e:
        messages.error(request, f"Hiba történt a törlés során: {str(e)}")
    return redirect("raktar:rendszam")

###########################################  ALKATRÉSZ 
@login_required
def alkatresz(request):
    alkatreszek = Alkatresz.objects.all().order_by('cikkszam')
    mertekegysegek = Mertekegyseg.objects.all()
    alkatreszcsoportok = Alkatreszcsoport.objects.all().order_by('alkcsop')
    context = {
        'alkatreszek': alkatreszek,
        'mertekegysegek': mertekegysegek,
        'alkatreszcsoportok': alkatreszcsoportok
    }
    return render(request,'alkatresz.html', context)

@login_required
def addAlkatresz(request):
    if request.method == "POST":
        try:
            newCikkszam = request.POST["ujCikkszam"]
            newLeiras = request.POST["ujLeiras"]
            newinfo = request.POST.get("ujInfo", "")  # get() használata, ha üres lehet
            newMertekegyseg = request.POST["ujMertekegyseg"]
            newMertekegysegPeldany = Mertekegyseg.objects.get(mertegys=newMertekegyseg)
            newAlkatreszCsoport = request.POST["ujAlkatreszCsoport"]
            newAlkatreszCsoportPeldany = Alkatreszcsoport.objects.get(alkcsop=newAlkatreszCsoport)
            newKeszlet = request.POST["ujKeszlet"]
            newListaar = request.POST["ujListaar"]
            
            newRekord = Alkatresz(
                cikkszam=newCikkszam,
                leiras=newLeiras,
                info=newinfo,
                mertekegyseg=newMertekegysegPeldany,
                alkatreszcsoport=newAlkatreszCsoportPeldany,
                keszlet=newKeszlet,
                listaar=newListaar
            )
            newRekord.save()
            messages.success(request, "Alkatrész sikeresen hozzáadva!")
        except Exception as e:
            messages.error(request, f"Hiba történt: {str(e)}")
    return redirect("raktar:alkatresz")

@login_required
def deleteAlkatreszById(request, alkatreszId):
    try:
        torlendoAlkatresz = Alkatresz.objects.get(pk=alkatreszId)
        torlendoAlkatresz.delete()
        messages.success(request, "Alkatrész sikeresen törölve!")
    except Exception as e:
        messages.error(request, f"Hiba történt a törlés során: {str(e)}")
    return redirect("raktar:alkatresz")

@login_required
def deleteAlkatreszByCikkszam(request):
    if request.method == "POST":
        try:
            torlendoAlkatreszCikkszam = request.POST["alkatreszCikkszam"]
            torlendoAlkatresz = Alkatresz.objects.get(cikkszam=torlendoAlkatreszCikkszam)
            torlendoAlkatresz.delete()
            messages.success(request, "Alkatrész sikeresen törölve!")
        except Exception as e:
            messages.error(request, f"Hiba történt a törlés során: {str(e)}")
    return redirect("raktar:alkatresz")

@login_required
def editAlkatreszById(request, alkatreszId):
    alkatresz = get_object_or_404(Alkatresz, id=alkatreszId)
    if request.method == "POST":
        form = AlkatreszForm(request.POST, instance=alkatresz)
        if form.is_valid():
            form.save()
            messages.success(request, "Alkatrész sikeresen módosítva!")
            return redirect('raktar:alkatresz')
        else:
            messages.error(request, "Hibás adatok! Kérjük ellenőrizze a mezőket.")
    else:
        form = AlkatreszForm(instance=alkatresz)
    return render(request, 'edit_alkatresz.html', {'form': form})

##########################   Bevételi Bizonylat
@login_required
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

@login_required
def addBebizonylat(request):
    if request.method == "POST":
        try:
            newSzallito = request.POST["ujSzallito"]
            newSzallitoPeldany = Beszallito.objects.get(beszallito=newSzallito)
            newSzamlaszam = request.POST.get("ujSzamlaszam", "")
            newSzallitolevelszam = request.POST.get("ujSzallitolevelszam", "")
            newDatum = request.POST["ujDatum"]

            alapadat = AlapAdat.objects.first()
            if not alapadat:
                messages.error(request, "Nincs beállítva AlapAdat rekord!")
                return redirect("raktar:bebizonylat")

            # Létrehozás genbizid nélkül
            newRekord = Bizonylat(
                szallito=newSzallitoPeldany,
                bizonylattipus=True,
                szamlaszam=newSzamlaszam,
                szallitolevelszam=newSzallitolevelszam,
                datum=newDatum,
                lezart=False
            )
            newRekord.save()
            
            # genbizid kiszámítása
            kulonbseg = newRekord.id - alapadat.maxBizId
            genbizid = f"BE{alapadat.ev}_{kulonbseg:04d}"
            newRekord.genbizid = genbizid
            newRekord.save(update_fields=["genbizid"])
            
            messages.success(request, f"Bevételi bizonylat sikeresen létrehozva! ({genbizid})")
        except Exception as e:
            messages.error(request, f"Hiba történt: {str(e)}")
    
    return redirect("raktar:bebizonylat")

@login_required
def bebizonylatsorok(request, pk):
    aktualis_bizonylat = get_object_or_404(Bizonylat, pk=pk)
    aktualis_alakterszek = Alkatresz.objects.all()
    aktualisbiz_sorai = aktualis_bizonylat.sorok.all()
    osszeg = 0
    for sor in aktualisbiz_sorai:
        osszeg += sor.aktualisar * sor.mennyiseg
    return render(request, "bebizonylatsorok.html", {
        "alkatreszek": aktualis_alakterszek,
        "bizonylat": aktualis_bizonylat,
        "sorok": aktualisbiz_sorai,
        "osszeg": f"{osszeg:,.0f} ft".replace(",", ".")
    })

@login_required
def addBebizonylatsor(request):
    if request.method == "POST":
        try:
            newBizonylatId = request.POST["bizonylat_id"]
            newBizonylatPeldany = Bizonylat.objects.get(id=newBizonylatId)
            newAlkatresz = request.POST["ujAlkatresz"]
            newAlkatreszPeldany = Alkatresz.objects.get(cikkszam=newAlkatresz)
            newMennyiseg = request.POST["ujMennyiseg"]
            newAktualisar = request.POST["ujAktualisar"]
            
            newRecord = Bizonylatsor(
                bizonylat=newBizonylatPeldany,
                alkatresz=newAlkatreszPeldany,
                mennyiseg=newMennyiseg,
                aktualisar=newAktualisar
            )
            newRecord.save()
            
            # Készlet frissítése
            newAlkatreszPeldany.keszlet += float(newMennyiseg)
            newAlkatreszPeldany.listaar = float(newAktualisar)
            newAlkatreszPeldany.save()
            
            messages.success(request, "Bizonylatsor sikeresen hozzáadva!")
        except Exception as e:
            messages.error(request, f"Hiba történt: {str(e)}")
    
    return redirect(request.META.get('HTTP_REFERER', 'raktar:bebizonylat'))

@login_required
def deleteBebizonylat(request, biz_id):
    try:
        rekord = get_object_or_404(Bizonylat, id=biz_id, bizonylattipus=True)
        rekord.delete()
        messages.success(request, "Bevételi bizonylat sikeresen törölve!")
    except Exception as e:
        messages.error(request, f"Hiba történt a törlés során: {str(e)}")
    return redirect("raktar:bebizonylat")

########################## KIVÉTELI BIZONYLATOK
@login_required
def kivbizonylat(request):
    kivbizonylatok = Bizonylat.objects.filter(bizonylattipus=False)
    rendszamok = Rendszam.objects.all()
    context = {
        'kivbizonylatok': kivbizonylatok,
        'rendszamok': rendszamok
    }
    return render(request, 'kivbizonylat.html', context)

@login_required
def addKivbizonylat(request):
    if request.method == "POST":
        try:
            newRendszam = request.POST["ujRendszam"]
            newRendszamPeldany = Rendszam.objects.get(rendszam=newRendszam)
            newDatum = request.POST["ujDatum"]

            alapadat = AlapAdat.objects.first()
            if not alapadat:
                messages.error(request, "Nincs beállítva AlapAdat rekord!")
                return redirect("raktar:kivbizonylat")

            newRekord = Bizonylat(
                rendszam=newRendszamPeldany,
                bizonylattipus=False,
                datum=newDatum,
                lezart=False
            )
            newRekord.save()
            
            # genbizid kiszámítása
            kulonbseg = newRekord.id - alapadat.maxBizId
            genbizid = f"KI{alapadat.ev}_{kulonbseg:04d}"
            newRekord.genbizid = genbizid
            newRekord.save(update_fields=["genbizid"])
            
            messages.success(request, f"Kivételi bizonylat sikeresen létrehozva! ({genbizid})")
        except Exception as e:
            messages.error(request, f"Hiba történt: {str(e)}")
    
    return redirect("raktar:kivbizonylat")

@login_required
def deleteKivbizonylat(request, biz_id):
    try:
        rekord = get_object_or_404(Bizonylat, id=biz_id, bizonylattipus=False)
        rekord.delete()
        messages.success(request, "Kivételi bizonylat sikeresen törölve!")
    except Exception as e:
        messages.error(request, f"Hiba történt a törlés során: {str(e)}")
    return redirect("raktar:kivbizonylat")

########################## LOGIN/LOGOUT
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        
        if user:
            login(request, user)
            return redirect("raktar:dashboard")
        else:
            messages.error(request, "Hibás felhasználónév vagy jelszó!")
    
    return render(request, "login.html")

@method_decorator(login_required, name='dispatch')
class DashboardView(TemplateView):
    """
    Fő dashboard oldal.
    Template: templates/dashboard.html
    """
    template_name = "dashboard.html"

@login_required
def leltar(request):
    alkatreszek = Alkatresz.objects.all().select_related('mertekegyseg', 'alkatreszcsoport')
    
    # Leltár adatok összesítése
    total_quantity = sum(float(a.keszlet) for a in alkatreszek)
    total_value = sum(float(a.keszlet) * float(a.listaar) for a in alkatreszek)
    
    context = {
        'alkatreszek': alkatreszek,
        'total_quantity': total_quantity,
        'total_value': total_value
    }
    return render(request, 'leltar.html', context)

def logout_view(request):
    logout(request)
    messages.info(request, "Sikeresen kijelentkezett!")
    return redirect('raktar:login')