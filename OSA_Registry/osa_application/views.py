from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Count
import csv, io
from django.db.models import Avg, Max, Min
from pyexpat.errors import messages

from .models import Patient, Firma, Vorscreening, Masken, Gerät, Schlafbetreuender_Arzt,DiagnosePSG,CPAP_Einstellung,CPAP_Kontrolle, Spontanous,Therapieabbruch,patient_medikamente,Medikament
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.core.paginator import Paginator





#Patient
@login_required(login_url='login')
@permission_required('osa_application.add_patient',login_url='login')
def postpatient_index(request):
    if request.user.is_authenticated:
        return render(request, 'postpatient.html')
    else:
        return redirect('')

@login_required(login_url='login')
@permission_required('osa_application.add_patient',login_url='login')
def postpatient(request):
    SVNummer = request.POST.get("svnummer")
    Geburtsdatum = request.POST.get("geburtsdatum")
    Vorname = request.POST.get("vorname")
    Nachname = request.POST.get("nachname")
    Geschlecht = request.POST.get("geschlecht")
    Vorscreening = request.POST.get("vorscreening")

    VerändertVon = request.user.id
    VerändertAm = datetime.datetime.now()
    Gelöscht = False

    anzahl = Patient.objects.order_by().values('PatientID').distinct().count()
    PatientID = anzahl + 1

    Version = 1

    if SVNummer == "":
        SVNummer = None

    if Geburtsdatum == "":
        Geburtsdatum = None

    if Vorscreening == "":
        Vorscreening = None

    insert_txt = Patient(PatientID=PatientID,Version=Version,SVNummer=SVNummer,Geburtsdatum=Geburtsdatum,Vorname=Vorname,Nachname=Nachname,Geschlecht=Geschlecht,Vorscreening=Vorscreening,VerändertAm=VerändertAm,VerändertVon=VerändertVon,Gelöscht=Gelöscht)
    insert_txt.save()

    return render(request,'post.html')

@login_required(login_url='login')
@permission_required('osa_application.view_patient',login_url='login')
def getpatient(request):
    all_patients = Patient.objects.filter(Gelöscht=False)
    return render(request,'getpatient.html', {"Patients": Paginator(all_patients, 3).page(request.GET.get('page') or 1)})

@login_required(login_url='login')
@permission_required('osa_application.delete_patient',login_url='login')
def deletepatient(request,id):
    delp = Patient.objects.get(id=id)
    delp.VerändertVon = request.user.id
    delp.VerändertAm = datetime.datetime.now()
    delp.Gelöscht = True
    delp.save()

    all_patients = Patient.objects.filter(Gelöscht=False)
    return render(request, 'getpatient.html', {"Patients": all_patients})

@login_required(login_url='login')
@permission_required('osa_application.update_patient',login_url='login')
def putpatient_index(request, id):
    ed = Patient.objects.get(id=id)
    return render(request,'editpatient.html', {"Patients":ed})

@login_required(login_url='login')
@permission_required('osa_application.update_patient',login_url='login')
def putpatient(request,id):


    SVNummer = request.POST.get("svnummer")
    Geburtsdatum = request.POST.get("geburtsdatum")
    Vorname = request.POST.get("vorname")
    Nachname = request.POST.get("nachname")
    Geschlecht = request.POST.get("geschlecht")
    Vorscreening = request.POST.get("vorscreening")
    VerändertVon = request.user
    VerändertAm = datetime.datetime.now()
    Gelöscht = False


    putpatient= Patient.objects.get(id=id)

    PatientID = putpatient.PatientID

    putpatient.VerändertVon = request.user.id
    putpatient.VerändertAm = datetime.datetime.now()
    putpatient.Gelöscht = True
    putpatient.save()

    anzahl = Patient.objects.filter(PatientID= PatientID).order_by().values('Version').distinct().count()

    Version = anzahl + 1


    if SVNummer == "":
        SVNummer = None

    if Geburtsdatum == "":
        Geburtsdatum = None

    if Vorscreening == "":
        Vorscreening = None

    insert_txt = Patient(SVNummer=SVNummer,Geburtsdatum=Geburtsdatum,Vorname=Vorname,Nachname=Nachname,Geschlecht=Geschlecht,Vorscreening=Vorscreening,VerändertAm=VerändertAm,VerändertVon=VerändertVon,Gelöscht=Gelöscht,PatientID=PatientID,Version=Version)


    insert_txt.save()

    all_patients = Patient.objects.filter(Gelöscht=False)
    return render(request,'getpatient.html', {"Patients": all_patients})

@login_required(login_url='login')
@permission_required('osa_application.view_patient_medikamente',login_url='login')
def getpatientmedikamente(request, id):
    ed = patient_medikamente.objects.filter(Patient=id)
    patient = Patient.objects.get(id=id)
    return render(request,'getpatientmedikamente.html', {"Medikamente":ed,"Patients":patient})

def suchepatient(request):
    suche = request.POST.get("suchen")
    suche_auf = request.POST.get("suche_auf")
    all_patients =  Patient.objects.filter(Gelöscht=False)

    if suche is None:
        suche = ""

        all_patients = Patient.objects.filter(Gelöscht=False, Vorname=suche) |Patient.objects.filter(Gelöscht=False, Geschlecht=suche)|Patient.objects.filter(Gelöscht=False, Nachname=suche)

    elif isinstance(suche, float) == True:
        all_patients = Patient.objects.filter(Gelöscht=False, SVNummer=suche)

    elif isinstance(suche, datetime) == True:
        all_patients = Patient.objects.filter(Gelöscht=False, Geburtsdatume=suche)
    return render(request,'getpatient.html', {"Patients": all_patients})


@login_required(login_url='login')
@permission_required('osa_application.add_patient_medikamente',login_url='login')
def postpatientmedikamente_index(request, id):
    ed = Patient.objects.get(id=id)
    medikament = Medikament.objects.filter()
    return render(request, 'postpatientmedikament.html',{"patient":ed,"Medikamente":medikament})

@login_required(login_url='login')
@permission_required('osa_application.add_patient_medikamente',login_url='login')
def postpatientmedikamente(request, id):
    me = request.POST.get("MedikamenteID")
    ed = Patient.objects.get(id=id)

    medikamente = Medikament.objects.all()

    VerändertVon = request.user.id
    VerändertAm = datetime.datetime.now()
    Gelöscht = False

    insert_txt = patient_medikamente(Patient=id,Medikament=me,VerändertAm=VerändertAm,VerändertVon=VerändertVon,Gelöscht=Gelöscht)
    insert_txt.save()

    return render(request, 'postpatientmedikament.html',{"patient":ed,"Medikamente":medikamente})

@login_required(login_url='login')
@permission_required('osa_application.delete_patient_medikamente',login_url='login')
def deltepatientmedikamente(request, id,p_id):

    ed = patient_medikamente.objects.filter(id=id)
    ed.delete()

    me = patient_medikamente.objects.filter()

    patient = Patient.objects.get(id=p_id)
    return render(request,'getpatientmedikamente.html', {"Medikamente":me,"Patients":patient})

@permission_required('osa_application.insert_medikamente',login_url='login')
def importmedikament(request):
    template = "importmedikament.html"
    if request.method == "GET":
        return render(request, template)

    csv_file = request.FILES['file']

    print(csv_file)
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'Bitte geben Sie eine csv Datei ab.')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)

    for column in csv.reader(io_string,delimiter=',', quotechar="|"):
        _, created = Medikament.objects.update_or_create(
            Bezeichnung=column[0],
        )
    return render(request,template)




#Firma
@login_required(login_url='login')
@permission_required('osa_application.add_firma',login_url='login')
def postfirma_index(request):
    return render(request, 'postfirma.html')

@login_required(login_url='login')
@permission_required('osa_application.add_firma',login_url='login')
def postfirma(request):
    Firmenname = request.POST.get("Firmenname")

    anzahl = Firma.objects.order_by().values('Set').distinct().count()
    Set = anzahl + 1

    Version = 1

    VerändertVon = request.user.id
    VerändertAm = datetime.datetime.now()
    Gelöscht = False

    insert_txt = Firma(Version=Version,Set=Set,Firmenname=Firmenname,VerändertVon=VerändertVon,VerändertAm=VerändertAm,Gelöscht=Gelöscht)
    insert_txt.save()

    return render(request,'postfirma.html',{"message": "registered!"})

@login_required(login_url='login')
@permission_required('osa_application.view_firma',login_url='login')
def getfirma(request):
    values = Firma.objects.filter(Gelöscht=False)
    return render(request,'getfirma.html', {"values": Paginator(values, 3).page(request.GET.get('page') or 1)})

def suchefirma(request):
    suche = request.POST.get("suchen")
    if suche is None:
        suche = ""
    values = Firma.objects.filter(Gelöscht=False, Firmenname=suche)
    return render(request,'getfirma.html', {"values": values})

@login_required(login_url='login')
@permission_required('osa_application.delete_firma',login_url='login')
def deletefirma(request,id):
    value = Firma.objects.get(id=id)

    value.VerändertVon = request.user.id
    value.VerändertAm = datetime.datetime.now()
    value.Gelöscht = True
    value.save()

    values = Firma.objects.filter(Gelöscht=False)
    return render(request, 'getfirma.html', {"values": values})

@login_required(login_url='login')
@permission_required('osa_application.change_firma',login_url='login')
def putfirma_index(request, id):
    value = Firma.objects.get(id=id)
    return render(request,'editfirma.html', {"values":value})

@login_required(login_url='login')
@permission_required('osa_application.change_firma',login_url='login')
def putfirma(request, id, SVNummer=None, Geburtsdatum=None, Vorname=None, Nachname=None, Geschlecht=None):
    value = Firma.objects.get(id=id)

    value.VerändertVon = request.user.id
    value.VerändertAm = datetime.datetime.now()
    value.Gelöscht = True
    value.save()

    VerändertVon = request.user.id
    VerändertAm = datetime.datetime.now()
    Gelöscht = False


    Set = value.Set

    anzahl = Firma.objects.filter(Set= Set).order_by().values('Version').distinct().count()

    Version = anzahl + 1

    insert_txt = Firma(Set=Set,Version=Version,SVNummer=SVNummer,Geburtsdatum=Geburtsdatum,Vorname=Vorname,Nachname=Nachname,Geschlecht=Geschlecht,Vorscreening=Vorscreening,VerändertAm=VerändertAm,VerändertVon=VerändertVon,Gelöscht=Gelöscht)
    insert_txt.save()

    values = Firma.objects.filter(Gelöscht=False)
    return render(request, 'getfirma.html', {"values": values})



#Vorscreening
@login_required(login_url='login')
@permission_required('osa_application.add_vorscreening',login_url='login')
def postvorscreening_index(request):
    values = Schlafbetreuender_Arzt.objects.filter(Gelöscht=False)
    return render(request, 'postvorscreening.html',{"values":values})


@login_required(login_url='login')
@permission_required('osa_application.add_vorscreening',login_url='login')
def postvorscreening(request):
    PGdurchgeführtvon = request.POST.get("PGdurchgeführtvon")
    DatumderPG = request.POST.get("DatumderPG")
    sao2minPG = request.POST.get("sao2minPG")
    RDI = request.POST.get("RDI")
    EingabeID = request.POST.get("EingabeID")

    anzahl = Vorscreening.objects.order_by().values('Set').distinct().count()
    Set = anzahl + 1

    Version = 1

    VerändertVon = request.user.id
    VerändertAm = datetime.datetime.now()
    Gelöscht = False

    if DatumderPG == "":
        DatumderPG = None
    if sao2minPG == "":
        sao2minPG = None
    if RDI == "":
        RDI = None



    insert_txt = Vorscreening(Set=Set,Version=Version,PGdurchgeführtvon=PGdurchgeführtvon,DatumderPG=DatumderPG,sao2minPG=sao2minPG,RDI=RDI,VerändertVon=VerändertVon,VerändertAm=VerändertAm,Gelöscht=Gelöscht)
    insert_txt.save()
    values = Vorscreening.objects.filter(Gelöscht=False)
    return render(request,'postvorscreening.html', {"values": values})

@login_required(login_url='login')
@permission_required('osa_application.view_vorscreening',login_url='login')
def getvorscreening(request):
    arzt = Schlafbetreuender_Arzt.objects.filter(Gelöscht=False)

    anzahl = Schlafbetreuender_Arzt.objects.all().values('Set').annotate(total=Count('Version'))
    values = Vorscreening.objects.filter(Gelöscht=False)
    return render(request,'getvorscreening.html', {"values": Paginator(values, 3).page(request.GET.get('page') or 1),"arzt":arzt,"anzahl":anzahl})


def suchevorscreening(request):
    suche = request.POST.get("suchen")
    if suche is None:
        suche = ""
    values = Vorscreening.objects.filter(Gelöscht=False, PGdurchgeführtvon=suche)| \
             Vorscreening.objects.filter(Gelöscht=False, DatumderPG=suche)|\
             Vorscreening.objects.filter(Gelöscht=False, sao2minPG=suche)|\
             Vorscreening.objects.filter(Gelöscht=False, RDI=suche)

    return render(request,'getvorscreening.html', {"values": values})


@login_required(login_url='login')
@permission_required('osa_application.delete_vorscreening',login_url='login')
def deletevorscreening(request,id):
    value = Vorscreening.objects.get(id=id)

    value.VerändertVon = request.user.id
    value.VerändertAm = datetime.datetime.now()
    value.Gelöscht = True
    value.save()

    values = Vorscreening.objects.filter(Gelöscht=False)
    return render(request,'getvorscreening.html', {"values": values})

@login_required(login_url='login')
@permission_required('osa_application.change_vorscreening',login_url='login')
def putvorscreening_index(request, id):
    value = Vorscreening.objects.get(id=id)
    values = Schlafbetreuender_Arzt.objects.filter(Gelöscht=False)
    return render(request,'editvorscreening.html', {"value":value,"values":values})

@login_required(login_url='login')
@permission_required('osa_application.change_vorscreening',login_url='login')
def putvorscreening(request,id):
    value = Vorscreening.objects.get(id=id)
    arzt = Schlafbetreuender_Arzt.objects.filter()

    value.VerändertVon = request.user.id
    value.VerändertAm = datetime.datetime.now()
    value.Gelöscht = True
    value.save()

    PGdurchgeführtvon = request.POST.get("PGdurchgeführtvon")
    DatumderPG = request.POST.get("PGdurchgeführtvon")
    sao2minPG = request.POST.get("sao2minPG")
    RDI = request.POST.get("RDI")
    #EingabeID = request.POST.get("EingabeID")

    Set = value.Set

    anzahl = Vorscreening.objects.filter(Set=Set).order_by().values('Version').distinct().count()

    Version = anzahl + 1

    if DatumderPG == "":
        DatumderPG = None
    if sao2minPG == "":
        sao2minPG = None
    if RDI == "":
        RDI = None

    VerändertVon = request.user.id
    VerändertAm = datetime.datetime.now()
    Gelöscht = False

    insert_txt = Vorscreening(Version=Version,Set=Set,PGdurchgeführtvon=PGdurchgeführtvon,DatumderPG=DatumderPG,sao2minPG=sao2minPG,RDI=RDI,VerändertVon=VerändertVon,VerändertAm=VerändertAm,Gelöscht=Gelöscht)
    insert_txt.save()

    values = Schlafbetreuender_Arzt.objects.filter(Gelöscht=False)

    return render(request,'editvorscreening.html', {"values": values})




#Masken
@login_required(login_url='login')
@permission_required('osa_application.add_masken',login_url='login')
def postmasken_index(request):
    all_patients = Patient.objects.filter(Gelöscht=False)
    return render(request, 'postmasken.html',{"patients":all_patients})

@login_required(login_url='login')
@permission_required('osa_application.add_masken',login_url='login')
def postmasken(request):
    PatientID = request.POST.get("PatientID")
    Maskentyp = request.POST.get("Maskentyp")
    Maskenname = request.POST.get("Maskenname")
    Hersteller = request.POST.get("Hersteller")
    Größe = request.POST.get("Größe")

    anzahl = Masken.objects.order_by().values('Set').distinct().count()
    Set = anzahl + 1

    Version = 1

    VerändertVon = request.user.id
    VerändertAm = datetime.datetime.now()
    Gelöscht = False

    if PatientID == "":
        PatientID = None
    if Größe == "":
        Größe = None

    insert_txt = Masken(Set=Set,Version=Version,PatientID=PatientID, Maskentyp=Maskentyp, Maskenname=Maskenname, Hersteller=Hersteller,
                              Größe=Größe, VerändertVon=VerändertVon, VerändertAm=VerändertAm,
                              Gelöscht=Gelöscht)
    insert_txt.save()

    values = Patient.objects.filter(Gelöscht=False)
    return render(request,'postmasken.html', {"patients": values})

@login_required(login_url='login')
@permission_required('osa_application.view_masken',login_url='login')
def getmasken(request):
    values = Masken.objects.filter(Gelöscht=False)
    all_patients = Patient.objects.filter(Gelöscht=False)

    anzahl = Patient.objects.all().values('PatientID').annotate(total=Count('Version'))

    return render(request,'getmasken.html', {"values": Paginator(values, 3).page(request.GET.get('page') or 1),"patients":all_patients,"anzahl":anzahl})

def sucheMasken(request):
    suche = request.POST.get("suchen")
    if suche is None:
        suche = ""
    values = Masken.objects.filter(Gelöscht=False, PatientID=suche)|\
             Masken.objects.filter(Gelöscht=False, Maskentyp=suche)|\
             Masken.objects.filter(Gelöscht=False, Maskenname=suche)|\
             Masken.objects.filter(Gelöscht=False, Hersteller=suche)|\
             Masken.objects.filter(Gelöscht=False, Größe=suche)
    return render(request,'getmasken.html', {"values": values})

@login_required(login_url='login')
@permission_required('osa_application.delete_masken',login_url='login')
def deletemasken(request, id):
    value = Masken.objects.get(id=id)

    value.VerändertVon = request.user.id
    value.VerändertAm = datetime.datetime.now()
    value.Gelöscht = True
    value.save()

    values = Masken.objects.filter(Gelöscht=False)
    return render(request,'getmasken.html', {"values": values})

@login_required(login_url='login')
@permission_required('osa_application.change_masken',login_url='login')
def putmasken_index(request, id):
    value = Masken.objects.get(id=id)
    return render(request, 'editmasken.html', {"values": value})

@login_required(login_url='login')
@permission_required('osa_application.change_masken',login_url='login')
def putmasken(request, id):
    value = Masken.objects.get(id=id)

    value.VerändertVon = request.user.id
    value.VerändertAm = datetime.datetime.now()
    value.Gelöscht = True
    value.save()

    PatientID = request.POST.get("PatientID")
    Maskentyp = request.POST.get("Maskentyp")
    Maskenname = request.POST.get("Maskenname")
    Hersteller = request.POST.get("Hersteller")
    Größe = request.POST.get("Größe")

    VerändertVon = request.user.id
    VerändertAm = datetime.datetime.now()
    Gelöscht = False

    Set = value.Set

    anzahl = Masken.objects.filter(Set=Set).order_by().values('Version').distinct().count()

    Version = anzahl + 1

    if PatientID == "":
        PatientID = None
    if Größe == "":
        Größe = None

    insert_txt = Masken(Version=Version,Set=Set,PatientID=PatientID, Maskentyp=Maskentyp, Maskenname=Maskenname, Hersteller=Hersteller,
                              Größe=Größe, VerändertVon=VerändertVon, VerändertAm=VerändertAm,
                              Gelöscht=Gelöscht)
    insert_txt.save()

    values = Masken.objects.filter(Gelöscht=False)
    return render(request,'getmasken.html', {"values": values})





#Gerät
@login_required(login_url='login')
@permission_required('osa_application.add_gerät',login_url='login')
def postgerät_index(request):
    all_patients = Patient.objects.filter(Gelöscht=False)
    return render(request, 'postgerät.html',{"patients":all_patients})

@login_required(login_url='login')
@permission_required('osa_application.add_gerät',login_url='login')
def postgerät(request):
    PatientID = request.POST.get("PatientID")
    Gerätename = request.POST.get("Gerätename")
    Hersteller = request.POST.get("Hersteller")
    vertreibendeFirma = request.POST.get("vertreibendeFirma")
    Modi = request.POST.get("Modi")
    WLB = request.POST.get("WLB")
    Rampe = request.POST.get("Rampe")
    O2Anschluss = request.POST.get("O2Anschluss")
    Heizschlauch = request.POST.get("Heizschlauch")
    Freitext = request.POST.get("Freitext")

    anzahl = Gerät.objects.order_by().values('Set').distinct().count()
    Set = anzahl + 1

    Version = 1

    if PatientID == "":
        PatientID = None
    if Modi == "":
        Modi = None
    if WLB == "":
        WLB = None
    if Rampe == "":
        Rampe = None
    if O2Anschluss == "":
        O2Anschluss = None
    if PatientID == "":
        PatientID = None
    if Heizschlauch == "":
        Heizschlauch = None

    VerändertVon = request.user
    VerändertAm = datetime.datetime.now()
    Gelöscht = False

    insert_txt = Gerät(Version=Version,Set=Set,PatientID=PatientID, Gerätename=Gerätename, Hersteller=Hersteller, vertreibendeFirma=vertreibendeFirma,
                              Modi=Modi,WLB=WLB,Rampe=Rampe,O2Anschluss=O2Anschluss, Heizschlauch=Heizschlauch,Freitext=Freitext, VerändertVon=VerändertVon, VerändertAm=VerändertAm,
                              Gelöscht=Gelöscht)
    insert_txt.save()
    values = Gerät.objects.filter(Gelöscht=False)
    return render(request, 'postgerät.html', {"values": values})

@login_required(login_url='login')
@permission_required('osa_application.view_gerät',login_url='login')
def getgerät(request):
    all_patients = Patient.objects.filter(Gelöscht=False)

    anzahl = Patient.objects.all().values('PatientID').annotate(total=Count('Version'))
    values = Gerät.objects.filter(Gelöscht=False)
    return render(request,'getgerät.html', {"values": Paginator(values, 3).page(request.GET.get('page') or 1),"patients":all_patients,"anzahl":anzahl})

def suchegerät(request):
    suche = request.POST.get("suchen")
    if suche is None:
        suche = ""
    values = Gerät.objects.filter(Gelöscht=False, PatientID=suche)|\
             Gerät.objects.filter(Gelöscht=False, Gerätename=suche)|\
             Gerät.objects.filter(Gelöscht=False, Hersteller=suche)|\
             Gerät.objects.filter(Gelöscht=False, vertreibendeFirma=suche)|\
             Gerät.objects.filter(Gelöscht=False, Modi=suche)|\
             Gerät.objects.filter(Gelöscht=False, WLB=suche)|\
             Gerät.objects.filter(Gelöscht=False, Rampe=suche)|\
             Gerät.objects.filter(Gelöscht=False, O2Anschluss=suche)|\
             Gerät.objects.filter(Gelöscht=False, Heizschlauch=suche)|\
             Gerät.objects.filter(Gelöscht=False, Freitext=suche)
    return render(request,'getgerät.html', {"values": values})

@login_required(login_url='login')
@permission_required('osa_application.delete_gerät',login_url='login')
def deletegerät(request, id):
    value = Gerät.objects.get(id=id)

    value.VerändertVon = request.user.id
    value.VerändertAm = datetime.datetime.now()
    value.Gelöscht = True
    value.save()

    values = Gerät.objects.filter(Gelöscht=False)
    return render(request, 'getgerät.html', {"values": values})

@login_required(login_url='login')
@permission_required('osa_application.change_gerät',login_url='login')
def putgerät_index(request, id):
    value = Gerät.objects.get(id=id)
    return render(request, 'editgerät.html', {"values": value})

@login_required(login_url='login')
@permission_required('osa_application.change_gerät',login_url='login')
def putgerät(request, id):
    value = Gerät.objects.get(id=id)

    value.VerändertVon = request.user.id
    value.VerändertAm = datetime.datetime.now()
    value.Gelöscht = True
    value.save()

    PatientID = request.POST.get("PatientID")
    Gerätename = request.POST.get("Gerätename")
    Hersteller = request.POST.get("Hersteller")
    vertreibendeFirma = request.POST.get("vertreibendeFirma")
    Modi = request.POST.get("Modi")
    WLB = request.POST.get("WLB")
    Rampe = request.POST.get("Rampe")
    O2Anschluss = request.POST.get("O2Anschluss")
    Heizschlauch = request.POST.get("Heizschlauch")
    Freitext = request.POST.get("Freitext")

    Set = value.Set

    anzahl = Gerät.objects.filter(Set=Set).order_by().values('Version').distinct().count()

    Version = anzahl + 1

    if PatientID == "":
        PatientID = None
    if Modi == "":
        Modi = None
    if WLB == "":
        WLB = None
    if Rampe == "":
        Rampe = None
    if O2Anschluss == "":
        O2Anschluss = None
    if PatientID == "":
        PatientID = None
    if Heizschlauch == "":
        Heizschlauch = None

    VerändertVon = request.user
    VerändertAm = datetime.datetime.now()
    Gelöscht = False

    insert_txt = Gerät(Set=Set,Version=Version,PatientID=PatientID, Gerätename=Gerätename, Hersteller=Hersteller, vertreibendeFirma=vertreibendeFirma,
                              Modi=Modi,WLB=WLB,Rampe=Rampe,O2Anschluss=O2Anschluss, Heizschlauch=Heizschlauch,Freitext=Freitext, VerändertVon=VerändertVon, VerändertAm=VerändertAm,
                              Gelöscht=Gelöscht)
    insert_txt.save()

    values = Gerät.objects.filter(Gelöscht=False)
    return render(request, 'getgerät.html', {"values": values})





#Schlafbetreuender
@login_required(login_url='login')
@permission_required('osa_application.add_schlafbetreuender_arzt',login_url='login')
def postschlafbetreuender_arzt_index(request):
    return render(request, 'postschlafbetreuender_arzt.html')

@login_required(login_url='login')
@permission_required('osa_application.add_schlafbetreuender_arzt',login_url='login')
def postschlafbetreuender_arzt(request):
    Vorhanden = request.POST.get("Vorhanden")
    Name = request.POST.get("Name")
    Fachrichtung = request.POST.get("Fachrichtung")
    plz = request.POST.get("plz")
    Ort = request.POST.get("Ort")
    Strasse = request.POST.get("Strasse")
    Hausnummer = request.POST.get("Hausnummer")
    Telefonnummer = request.POST.get("Telefonnummer")
    Email = request.POST.get("Email")
    #ArztID = request.POST.get("ArztID")

    VerändertVon = request.user.id
    VerändertAm = datetime.datetime.now()
    Gelöscht = False

    anzahl = Schlafbetreuender_Arzt.objects.order_by().values('Set').distinct().count()
    Set = anzahl + 1

    Version = 1

    if plz == "":
        plz = None
    if Strasse == "":
        Strasse = None
    if Hausnummer == "":
        Hausnummer = None
    if Telefonnummer == "":
        Telefonnummer = None


    insert_txt = Schlafbetreuender_Arzt(Set=Set,Version=Version,Vorhanden=Vorhanden, Name=Name, Fachrichtung=Fachrichtung, plz=plz,
                              Ort=Ort,Strasse=Strasse,Hausnummer=Hausnummer,Telefonnummer=Telefonnummer, Email=Email, VerändertVon=VerändertVon, VerändertAm=VerändertAm,
                              Gelöscht=Gelöscht)
    insert_txt.save()

    return render(request, 'postschlafbetreuender_arzt.html', {"message": "registered!"})

@login_required(login_url='login')
@permission_required('osa_application.view_schlafbetreuender_arzt',login_url='login')
def getschlafbetreuender_arzt(request):
    values = Schlafbetreuender_Arzt.objects.filter(Gelöscht=False)
    return render(request, 'getschlafbetreuender_arzt.html', {"values": Paginator(values, 3).page(request.GET.get('page') or 1)})

def suchearzt(request):
    suche = request.POST.get("suchen")
    if suche is None:
        suche = ""
    values = Schlafbetreuender_Arzt.objects.filter(Gelöscht=False, Vorhanden=suche)|\
             Schlafbetreuender_Arzt.objects.filter(Gelöscht=False, Name=suche)|\
             Schlafbetreuender_Arzt.objects.filter(Gelöscht=False, Fachrichtung=suche)|\
             Schlafbetreuender_Arzt.objects.filter(Gelöscht=False, plz=suche)|\
             Schlafbetreuender_Arzt.objects.filter(Gelöscht=False, Ort=suche)|\
             Schlafbetreuender_Arzt.objects.filter(Gelöscht=False, Strasse=suche)|\
             Schlafbetreuender_Arzt.objects.filter(Gelöscht=False, Hausnummer=suche)|\
             Schlafbetreuender_Arzt.objects.filter(Gelöscht=False, Telefonnummer=suche)|\
             Schlafbetreuender_Arzt.objects.filter(Gelöscht=False, Email=suche)
    return render(request,'getschlafbetreuender_arzt.html', {"values": values})

@login_required(login_url='login')
@permission_required('osa_application.delete_schlafbetreuender_arzt',login_url='login')
def deleteschlafbetreuender_arzt(request, id):
    value = Schlafbetreuender_Arzt.objects.get(id=id)

    value.VerändertVon = request.user.id
    value.VerändertAm = datetime.datetime.now()
    value.Gelöscht = True
    value.save()

    values = Schlafbetreuender_Arzt.objects.all()
    return render(request, 'getschlafbetreuender_arzt.html', {"values": values})

@login_required(login_url='login')
@permission_required('osa_application.change_schlafbetreuender_arzt',login_url='login')
def putschlafbetreuender_arzt_index(request, id):
    values = Schlafbetreuender_Arzt.objects.filter(Gelöscht=False)
    return render(request, 'getschlafbetreuender_arzt.html', {"values": values})

@login_required(login_url='login')
@permission_required('osa_application.change_schlafbetreuender_arzt',login_url='login')
def putschlafbetreudener_arzt(request, id):
    value = Schlafbetreuender_Arzt.objects.get(id=id)

    value.VerändertVon = request.user.id
    value.VerändertAm = datetime.datetime.now()
    value.Gelöscht = True
    value.save()

    Vorhanden = request.POST.get("Vorhanden")
    Name = request.POST.get("Name")
    Fachrichtung = request.POST.get("Fachrichtung")
    plz = request.POST.get("plz")
    Ort = request.POST.get("Ort")
    Strasse = request.POST.get("Strasse")
    Hausnummer = request.POST.get("Hausnummer")
    Telefonnummer = request.POST.get("Telefonnummer")
    Email = request.POST.get("Email")
    ArztID = request.POST.get("ArztID")

    VerändertVon = request.user.id
    VerändertAm = datetime.datetime.now()
    Gelöscht = False

    Set = value.Set

    anzahl = Schlafbetreuender_Arzt.objects.filter(Set=Set).order_by().values('Version').distinct().count()

    Version = anzahl + 1

    if plz == "":
        plz = None
    if Strasse == "":
        Strasse = None
    if Hausnummer == "":
        Hausnummer = None
    if Telefonnummer == "":
        Telefonnummer = None
    if ArztID == "":
        ArztID = None

    insert_txt = Schlafbetreuender_Arzt(Version=Version,Set=Set,Vorhanden=Vorhanden, Name=Name, Fachrichtung=Fachrichtung, plz=plz,
                              Ort=Ort,Strasse=Strasse,Hausnummer=Hausnummer,Telefonnummer=Telefonnummer, Email=Email,ArztID=ArztID, VerändertVon=VerändertVon, VerändertAm=VerändertAm,
                              Gelöscht=Gelöscht)
    insert_txt.save()

    values = Schlafbetreuender_Arzt.objects.filter(Gelöscht=False)
    return render(request, 'getschlafbetreuender_arzt.html', {"values": values})





#DiagnosePSG
@login_required(login_url='login')
@permission_required('osa_application.add_diagnosepsg',login_url='login')
def postdiagnosepsg_index(request):
    values = Patient.objects.filter(Gelöscht=False)
    return render(request, 'postdiagnosepsg.html', {"patients": values})


@login_required(login_url='login')
@permission_required('osa_application.add_diagnosepsg',login_url='login')
def postdiagnosepsg(request):
    PatientID = request.POST.get("PatientID")
    Datum_Diagnose_PSG = request.POST.get("Datum_Diagnose_PSG")
    BMI_bei_Diagnose_PSG = request.POST.get("BMI_bei_Diagnose_PSG")
    SaO2min_PSG = request.POST.get("SaO2min_PSG")
    Dominanz = request.POST.get("Dominanz")
    Lageabhängig = request.POST.get("Lageabhängig")
    AHI_Gesamt = request.POST.get("AHI_Gesamt")
    REM_assoziert = request.POST.get("REM_assoziert")
    O2unter90Prozent = request.POST.get("O2unter90Prozent")
    Diagnose = request.POST.get("Diagnose")
    Zustimmung_für_Beatmung = request.POST.get("Zustimmung_für_Beatmung")
    alternative_Therapieempfehlung = request.POST.get("alternative_Therapieempfehlung")
    primäre_Therapieempfehlung = request.POST.get("primäre_Therapieempfehlung")


    anzahl = DiagnosePSG.objects.order_by().values('Set').distinct().count()
    Set = anzahl + 1

    Version = 1

    VerändertVon = request.user.id
    VerändertAm = datetime.datetime.now()
    Gelöscht = False

    if Datum_Diagnose_PSG == "":
        Datum_Diagnose_PSG = None
    if BMI_bei_Diagnose_PSG == "":
        BMI_bei_Diagnose_PSG = None
    if SaO2min_PSG == "":
        SaO2min_PSG = None
    if Dominanz == "":
        Dominanz = None
    if Lageabhängig == "":
        Lageabhängig = None
    if AHI_Gesamt == "":
        AHI_Gesamt = None
    if REM_assoziert == "":
        REM_assoziert = None
    if O2unter90Prozent == "":
        O2unter90Prozent = None
    if REM_assoziert == "":
        REM_assoziert = None


    insert_txt = DiagnosePSG(Set=Set,Version=Version,PatientID=PatientID,Datum_Diagnose_PSG=Datum_Diagnose_PSG, BMI_bei_Diagnose_PSG=BMI_bei_Diagnose_PSG, SaO2min_PSG=SaO2min_PSG, Dominanz=Dominanz,
                              Lageabhängig=Lageabhängig,AHI_Gesamt=AHI_Gesamt,REM_assoziert=REM_assoziert,O2unter90Prozent=O2unter90Prozent, Diagnose=Diagnose,primäre_Therapieempfehlung=primäre_Therapieempfehlung,alternative_Therapieempfehlung=alternative_Therapieempfehlung,Zustimmung_für_Beatmung=Zustimmung_für_Beatmung, VerändertVon=VerändertVon, VerändertAm=VerändertAm,
                              Gelöscht=Gelöscht)
    insert_txt.save()

    values = Patient.objects.filter(Gelöscht=False)
    return render(request, 'postdiagnosepsg.html', {"patients": values})

@login_required(login_url='login')
@permission_required('osa_application.view_diagnosepsg',login_url='login')
def getdiagnosepsg(request):

    all_patients = Patient.objects.filter(Gelöscht=False)

    anzahl = Patient.objects.all().values('PatientID').annotate(total=Count('Version'))
    values = DiagnosePSG.objects.filter(Gelöscht=False)
    return render(request,'getdiagnosepsg.html', {"values": Paginator(values, 3).page(request.GET.get('page') or 1),"patients":Paginator(all_patients, 3).page(request.GET.get('page') or 1),"anzahl":Paginator(anzahl, 3).page(request.GET.get('page') or 1)})

def suchediagnose(request):
    suche = request.POST.get("suchen")
    if suche is None:
        suche = ""
    values = DiagnosePSG.objects.filter(Gelöscht=False, PatientID=suche)|\
             DiagnosePSG.objects.filter(Gelöscht=False, Datum_Diagnose_PSG=suche)|\
             DiagnosePSG.objects.filter(Gelöscht=False, BMI_bei_Diagnose_PSG=suche)|\
             DiagnosePSG.objects.filter(Gelöscht=False, SaO2min_PSG=suche)|\
             DiagnosePSG.objects.filter(Gelöscht=False, Dominanz=suche)|\
             DiagnosePSG.objects.filter(Gelöscht=False, Lageabhängig=suche)|\
             DiagnosePSG.objects.filter(Gelöscht=False, AHI_Gesamt=suche)|\
             DiagnosePSG.objects.filter(Gelöscht=False, REM_assoziert=suche)|\
             DiagnosePSG.objects.filter(Gelöscht=False, Diagnose=suche)|\
             DiagnosePSG.objects.filter(Gelöscht=False, O2unter90Prozent=suche)|\
             DiagnosePSG.objects.filter(Gelöscht=False, primäre_Therapieempfehlung=suche)|\
             DiagnosePSG.objects.filter(Gelöscht=False, alternative_Therapieempfehlung=suche)|\
             DiagnosePSG.objects.filter(Gelöscht=False, Zustimmung_für_Beatmung=suche)
    return render(request,'getdiagnosepsg.html', {"values": values})

@login_required(login_url='login')
@permission_required('osa_application.delete_diagnosepsg',login_url='login')
def deletediagnosepsg(request, id):
    value = DiagnosePSG.objects.get(id=id)

    value.VerändertVon = request.id
    value.VerändertAm = datetime.datetime.now()
    value.Gelöscht = True
    value.save()

    values = DiagnosePSG.objects.filter(Gelöscht=False)
    return render(request, 'getdiagnosepsg.html', {"values": values})

@login_required(login_url='login')
@permission_required('osa_application.change_diagnosepsg',login_url='login')
def putdiagnosepsg_index(request, id):
    value = DiagnosePSG.objects.get(id=id)
    return render(request, 'editdiagnosepsg.html', {"values": value})

@login_required(login_url='login')
@permission_required('osa_application.change_diagnosepsg',login_url='login')
def putdiagnosepsg(request, id):
    value = DiagnosePSG.objects.get(id=id)

    value.VerändertVon = request.user.id
    value.VerändertAm = datetime.datetime.now()
    value.Gelöscht = True
    value.save()

    Datum_Diagnose_PSG = request.POST.get("Datum_Diagnose_PSG")
    BMI_bei_Diagnose_PSG = request.POST.get("BMI_bei_Diagnose_PSG")
    SaO2min_PSG = request.POST.get("SaO2min_PSG")
    Dominanz = request.POST.get("Dominanz")
    Lageabhängig = request.POST.get("Lageabhängig")
    AHI_Gesamt = request.POST.get("AHI_Gesamt")
    REM_assoziert = request.POST.get("REM_assoziert")
    O2unter90Prozent = request.POST.get("O2unter90Prozent")
    Diagnose = request.POST.get("Diagnose")
    Zustimmung_für_Beatmung = request.POST.get("Zustimmung_für_Beatmung")
    alternative_Therapieempfehlung = request.POST.get("alternative_Therapieempfehlung")
    primäre_Therapieempfehlung = request.POST.get("primäre_Therapieempfehlung")

    Set = value.Set

    anzahl = DiagnosePSG.objects.filter(Set=Set).order_by().values('Version').distinct().count()

    Version = anzahl + 1

    VerändertVon = request.user.id
    VerändertAm = datetime.datetime.now()
    Gelöscht = False

    if Datum_Diagnose_PSG == "":
        Datum_Diagnose_PSG = None
    if BMI_bei_Diagnose_PSG == "":
        BMI_bei_Diagnose_PSG = None
    if SaO2min_PSG == "":
        SaO2min_PSG = None
    if Dominanz == "":
        Dominanz = None
    if Lageabhängig == "":
        Lageabhängig = None
    if AHI_Gesamt == "":
        AHI_Gesamt = None
    if REM_assoziert == "":
        REM_assoziert = None
    if O2unter90Prozent == "":
        O2unter90Prozent = None
    if REM_assoziert == "":
        REM_assoziert = None

    insert_txt = DiagnosePSG(Version=Version,Set=Set,Datum_Diagnose_PSG=Datum_Diagnose_PSG, BMI_bei_Diagnose_PSG=BMI_bei_Diagnose_PSG, SaO2min_PSG=SaO2min_PSG, Dominanz=Dominanz,
                              Lageabhängig=Lageabhängig,AHI_Gesamt=AHI_Gesamt,REM_assoziert=REM_assoziert,O2unter90Prozent=O2unter90Prozent, Diagnose=Diagnose,primäre_Therapieempfehlung=primäre_Therapieempfehlung,alternative_Therapieempfehlung=alternative_Therapieempfehlung,Zustimmung_für_Beatmung=Zustimmung_für_Beatmung, VerändertVon=VerändertVon, VerändertAm=VerändertAm,
                              Gelöscht=Gelöscht)
    insert_txt.save()

    values = DiagnosePSG.objects.filter(Gelöscht=False)
    return render(request, 'getdiagnosepsg.html', {"values": values})





#CPAP_Einstellung
@login_required(login_url='login')
@permission_required('osa_application.add_cpap_einstellung',login_url='login')
def postcpap_einstellung_index(request):
    all_patients = Patient.objects.filter(Gelöscht=False)
    return render(request, 'postcpap_einstellung.html',{"patients":all_patients})

@login_required(login_url='login')
@permission_required('osa_application.add_cpap_einstellung',login_url='login')
def postcpap_einstellung(request):
    PatientID = request.POST.get("PatientID")
    Datum_cpap = request.POST.get("Datum_cpap")

    minEPAP = request.POST.get("minEPAP")
    maxEPAP = request.POST.get("maxEPAP")
    minPS = request.POST.get("minPS")
    maxPS = request.POST.get("maxPS")
    Zielvolumen = request.POST.get("Zielvolumen")
    BeatmungsModi = request.POST.get("BeatmungsModi")
    IPAP = request.POST.get("IPAP")
    Erweitert = request.POST.get("Erweitert")

    anzahl = CPAP_Einstellung.objects.order_by().values('Set').distinct().count()
    Set = anzahl + 1

    Version = 1

    VerändertVon = request.user.id
    VerändertAm = datetime.datetime.now()
    Gelöscht = False


    insert_txt = CPAP_Einstellung(Version=Version,Set=Set,PatientID=PatientID, Datum_cpap=Datum_cpap, BeatmungsModi=BeatmungsModi,
                              IPAP=IPAP,minEPAP=minEPAP,maxEPAP=maxEPAP,minPS=minPS,maxPS=maxPS,Zielvolumen=Zielvolumen,Erweitert=Erweitert, VerändertVon=VerändertVon, VerändertAm=VerändertAm,
                              Gelöscht=Gelöscht)
    insert_txt.save()
    values = CPAP_Einstellung.objects.filter(Gelöscht=False)
    return render(request, 'postcpap_einstellung.html', {"values": values})

@login_required(login_url='login')
@permission_required('osa_application.view_cpap_einstellung',login_url='login')
def getcpap_einstellung(request):


    all_patients = Patient.objects.filter(Gelöscht=False)

    anzahl = Patient.objects.all().values('PatientID').annotate(total=Count('Version'))
    values = CPAP_Einstellung.objects.filter(Gelöscht=False)
    return render(request,'getcpap_einstellung.html', {"values": Paginator(values, 3).page(request.GET.get('page') or 1),"patients":Paginator(all_patients, 3).page(request.GET.get('page') or 1),"anzahl":Paginator(anzahl, 3).page(request.GET.get('page') or 1)})


def suchecpap_ein(request):
    suche = request.POST.get("suchen")
    if suche is None:
        suche = ""
    values = CPAP_Einstellung.objects.filter(Gelöscht=False, PatientID=suche)|\
             CPAP_Einstellung.objects.filter(Gelöscht=False, Datum_cpap=suche)|\
             CPAP_Einstellung.objects.filter(Gelöscht=False, minEPAP=suche)|\
             CPAP_Einstellung.objects.filter(Gelöscht=False, maxEPAP=suche)|\
             CPAP_Einstellung.objects.filter(Gelöscht=False, minPS=suche)|\
             CPAP_Einstellung.objects.filter(Gelöscht=False, maxPS=suche)|\
             CPAP_Einstellung.objects.filter(Gelöscht=False, IPAP=suche)|\
             CPAP_Einstellung.objects.filter(Gelöscht=False, Zielvolumen=suche)|\
             CPAP_Einstellung.objects.filter(Gelöscht=False, BeatmungsModi=suche)|\
             CPAP_Einstellung.objects.filter(Gelöscht=False, Erweitert=suche)
    return render(request,'getcpap_einstellung.html', {"values": values})

@login_required(login_url='login')
@permission_required('osa_application.delete_cpap_einstellung',login_url='login')
def deletecpap_einstellung(request, id):
    value = CPAP_Einstellung.objects.get(id=id)

    value.VerändertVon = request.user.id
    value.VerändertAm = datetime.datetime.now()
    value.Gelöscht = True
    value.save()

    values = CPAP_Einstellung.objects.filter(Gelöscht=False)
    return render(request, 'getcpap_einstellung.html', {"values": values})

@login_required(login_url='login')
@permission_required('osa_application.change_cpap_einstellung',login_url='login')
def putcpap_einstellung_index(request, id):
    value = CPAP_Einstellung.objects.get(id=id)
    return render(request, 'editcpap_einstellung.html', {"values": value})

@login_required(login_url='login')
@permission_required('osa_application.change_cpap_einstellung',login_url='login')
def putcpap_einstellung(request, id, EPAP=None):
    value = CPAP_Einstellung.objects.get(id=id)

    value.VerändertVon = request.user.id
    value.VerändertAm = datetime.datetime.now()
    value.Gelöscht = True
    value.save()

    PatientID = request.POST.get("PatientID")
    Datum_cpap = request.POST.get("Datum_cpap")

    minEPAP = request.POST.get("minEPAP")
    maxEPAP = request.POST.get("maxEPAP")
    minPS = request.POST.get("minPS")
    maxPS = request.POST.get("maxPS")
    Zielvolumen = request.POST.get("Zielvolumen")
    BeatmungsModi = request.POST.get("BeatmungsModi")
    IPAP = request.POST.get("IPAP")
    Erweitert = request.POST.get("Erweitert")

    VerändertVon = request.user.id
    VerändertAm = datetime.datetime.now()
    Gelöscht = False

    Set = value.Set

    anzahl = CPAP_Einstellung.objects.filter(Set=Set).order_by().values('Version').distinct().count()

    Version = anzahl + 1

    if PatientID == "":
        PatientID = None
    if Datum_cpap == "":
        Datum_cpap = None
    if IPAP == "":
        IPAP = None
    if EPAP == "":
        EPAP = None


    insert_txt = CPAP_Einstellung(Version=Version,Set=Set,PatientID=PatientID, Datum_cpap=Datum_cpap, BeatmungsModi=BeatmungsModi,
                              IPAP=IPAP,minEPAP=minEPAP,maxEPAP=maxEPAP,minPS=minPS,maxPS=maxPS,Zielvolumen=Zielvolumen,Erweitert=Erweitert, VerändertVon=VerändertVon, VerändertAm=VerändertAm,
                              Gelöscht=Gelöscht)
    insert_txt.save()
    values = CPAP_Einstellung.objects.filter(Gelöscht=False)
    return render(request, 'getcpap_einstellung.html', {"values": values})





#CPAP_Kontrolle
@login_required(login_url='login')
@permission_required('osa_application.add_cpap_kontrolle',login_url='login')
def postcpap_kontrolle_index(request):
    values = Patient.objects.filter(Gelöscht=False)
    return render(request, 'postcpap_kontrolle.html',{"patients":values})

@login_required(login_url='login')
@permission_required('osa_application.add_cpap_kontrolle',login_url='login')
def postcpap_kontrolle(request):
    PatientID = request.POST.get("PatientID")
    Datum_cpap = request.POST.get("Datum_cpap")
    Compliance_cpap = request.POST.get("Compliance_cpap")
    durchschnittlicheVerwendungsdauer = request.POST.get("durchschnittlicheVerwendungsdauer")
    berücksichtigteTage_CPAP = request.POST.get("berücksichtigteTage_CPAP")
    restAHibei_CPAP = request.POST.get("restAHibei_CPAP")
    nachjustierungNotwendig = request.POST.get("nachjustierungNotwendig")
    ModuswechselNotwendig = request.POST.get("ModuswechselNotwendig")

    VerändertVon = request.user
    VerändertAm = datetime.datetime.now()
    Gelöscht = False

    anzahl = CPAP_Kontrolle.objects.order_by().values('Set').distinct().count()
    Set = anzahl + 1

    Version = 1

    if PatientID == "":
        PatientID = None
    if Datum_cpap == "":
        Datum_cpap = None
    if durchschnittlicheVerwendungsdauer == "":
        durchschnittlicheVerwendungsdauer = None
    if berücksichtigteTage_CPAP == "":
        berücksichtigteTage_CPAP = None
    if restAHibei_CPAP == "":
        restAHibei_CPAP = None

    insert_txt = CPAP_Kontrolle(Version=Version,Set=Set,PatientID=PatientID, Datum_cpap=Datum_cpap, Compliance_cpap=Compliance_cpap, durchschnittlicheVerwendungsdauer=durchschnittlicheVerwendungsdauer,
                              berücksichtigteTage_CPAP=berücksichtigteTage_CPAP,restAHibei_CPAP=restAHibei_CPAP, nachjustierungNotwendig=nachjustierungNotwendig,ModuswechselNotwendig=ModuswechselNotwendig,VerändertVon=VerändertVon, VerändertAm=VerändertAm,
                              Gelöscht=Gelöscht)
    insert_txt.save()

    values = Patient.objects.filter(Gelöscht=False)
    return render(request, 'postcpap_kontrolle.html', {"patients": values})

@login_required(login_url='login')
@permission_required('osa_application.view_cpap_kontrolle',login_url='login')
def getcpap_kontrolle(request):

    all_patients = Patient.objects.filter(Gelöscht=False)

    anzahl = Patient.objects.all().values('PatientID').annotate(total=Count('Version'))

    values = CPAP_Kontrolle.objects.filter(Gelöscht=False)

    return render(request,'getcpap_kontrolle.html', {"values": Paginator(values, 3).page(request.GET.get('page') or 1),"patients":Paginator(all_patients, 3).page(request.GET.get('page') or 1),"anzahl":Paginator(anzahl, 3).page(request.GET.get('page') or 1)})


def suchecpap_kon(request):
    suche = request.POST.get("suchen")
    if suche is None:
        suche = ""
    values = CPAP_Kontrolle.objects.filter(Gelöscht=False, PatientID=suche)|\
             CPAP_Kontrolle.objects.filter(Gelöscht=False, Datum_cpap=suche)|\
             CPAP_Kontrolle.objects.filter(Gelöscht=False, Compliance_cpap=suche)|\
             CPAP_Kontrolle.objects.filter(Gelöscht=False, durchschnittlicheVerwendungsdauer=suche)|\
             CPAP_Kontrolle.objects.filter(Gelöscht=False, berücksichtigteTage_CPAP=suche)|\
             CPAP_Kontrolle.objects.filter(Gelöscht=False, restAHibei_CPAP=suche)|\
             CPAP_Kontrolle.objects.filter(Gelöscht=False, nachjustierungNotwendig=suche)|\
             CPAP_Kontrolle.objects.filter(Gelöscht=False, ModuswechselNotwendig=suche)
    return render(request,'getcpap_kontrolle.html', {"values": values})

@login_required(login_url='login')
@permission_required('osa_application.delete_cpap_kontrolle',login_url='login')
def deletecpap_kontrolle(request, id):
    value = CPAP_Kontrolle.objects.get(id=id)

    value.VerändertVon = request.user
    value.VerändertAm = datetime.datetime.now()
    value.Gelöscht = True
    value.save()

    values = CPAP_Kontrolle.objects.filter(Gelöscht=False)
    return render(request, 'getcpap_kontrolle.html', {"values": values})

@login_required(login_url='login')
@permission_required('osa_application.change_cpap_kontrolle',login_url='login')
def putcpap_kontrolle_index(request, id):
    value = CPAP_Kontrolle.objects.get(id=id)
    return render(request, 'editcpap_kontrolle.html', {"values": value})

@login_required(login_url='login')
@permission_required('osa_application.change_cpap_kontrolle',login_url='login')
def putcpap_kontrolle(request, id):
    value = CPAP_Kontrolle.objects.get(id=id)

    value.VerändertVon = request.user.id
    value.VerändertAm = datetime.datetime.now()
    value.Gelöscht = True
    value.save()

    PatientID = request.POST.get("PatientID")
    Datum_cpap = request.POST.get("Datum_cpap")
    Compliance_cpap = request.POST.get("Compliance_cpap")
    durchschnittlicheVerwendungsdauer = request.POST.get("durchschnittlicheVerwendungsdauer")
    berücksichtigteTage_CPAP = request.POST.get("berücksichtigteTage_CPAP")
    restAHibei_CPAP = request.POST.get("restAHibei_CPAP")
    nachjustierungNotwendig = request.POST.get("restAHibei_CPAP")
    ModuswechselNotwendig = request.POST.get("ModuswechselNotwendig")


    VerändertVon = request.user.id
    VerändertAm = datetime.datetime.now()
    Gelöscht = False

    if PatientID == "":
        PatientID = None
    if Datum_cpap == "":
        Datum_cpap = None
    if durchschnittlicheVerwendungsdauer == "":
        durchschnittlicheVerwendungsdauer = None
    if berücksichtigteTage_CPAP == "":
        berücksichtigteTage_CPAP = None
    if restAHibei_CPAP == "":
        restAHibei_CPAP = None

        Set = value.Set

        anzahl = CPAP_Kontrolle.objects.filter(Set=Set).order_by().values('Version').distinct().count()

        Version = anzahl + 1

    insert_txt = CPAP_Kontrolle(Version=Version,Set=Set,PatientID=PatientID, Datum_cpap=Datum_cpap, Compliance_cpap=Compliance_cpap, durchschnittlicheVerwendungsdauer=durchschnittlicheVerwendungsdauer,
                              berücksichtigteTage_CPAP=berücksichtigteTage_CPAP,restAHibei_CPAP=restAHibei_CPAP, nachjustierungNotwendig=nachjustierungNotwendig,ModuswechselNotwendig=ModuswechselNotwendig,VerändertVon=VerändertVon, VerändertAm=VerändertAm,
                              Gelöscht=Gelöscht)
    insert_txt.save()

    values = CPAP_Kontrolle.objects.filter(Gelöscht=False)
    return render(request, 'getcpap_kontrolle.html', {"values": values})





#Spontanous
@login_required(login_url='login')
@permission_required('osa_application.add_spontanous',login_url='login')
def postspontanous_index(request):
    all_patients = Patient.objects.filter(Gelöscht=False)
    return render(request, 'postspontanous.html',{"patients":all_patients})

@login_required(login_url='login')
@permission_required('osa_application.add_spontanous',login_url='login')
def postspontanous(request):
    #eingabeID = request.POST.get("eingabeID")
    PatientID = request.POST.get("PatientID")
    IPAP = request.POST.get("IPAP")
    EPAP = request.POST.get("EPAP")
    DeltaP = request.POST.get("DeltaP")
    verordnetam = request.POST.get("verordnetam")

    if PatientID == "":
        PatientID = None
    if IPAP == "":
        IPAP = None
    if EPAP == "":
        EPAP = None
    if DeltaP == "":
        DeltaP = None
    if verordnetam == "":
        verordnetam = None


    VerändertVon = request.user.id
    VerändertAm = datetime.datetime.now()
    Gelöscht = False

    anzahl = Firma.objects.order_by().values('Set').distinct().count()
    Set = anzahl + 1

    Version = 1

    insert_txt = Spontanous(Set=Set,Version=Version,PatientID=PatientID, IPAP=IPAP, EPAP=EPAP,
                              DeltaP=DeltaP, verordnetam=verordnetam,VerändertVon=VerändertVon, VerändertAm=VerändertAm,
                              Gelöscht=Gelöscht)
    insert_txt.save()
    values = Spontanous.objects.filter(Gelöscht=False)
    return render(request, 'postspontanous.html', {"values": values})

@login_required(login_url='login')
@permission_required('osa_application.view_spontanous',login_url='login')
def getspontanous(request):
    all_patients = Patient.objects.filter(Gelöscht=False)

    anzahl = Patient.objects.all().values('PatientID').annotate(total=Count('Version'))
    values = Spontanous.objects.filter(Gelöscht=False)
    return render(request,'getspontanous.html', {"values": Paginator(values, 3).page(request.GET.get('page') or 1),"patients":Paginator(all_patients, 3).page(request.GET.get('page') or 1),"anzahl":Paginator(anzahl, 3).page(request.GET.get('page') or 1)})

def suchespontanous(request):
    suche = request.POST.get("suchen")
    if suche is None:
        suche = ""
    values = Spontanous.objects.filter(Gelöscht=False, PatientID=suche)|Spontanous.objects.filter(Gelöscht=False, IPAP=suche)|Spontanous.objects.filter(Gelöscht=False, EPAP=suche)|Spontanous.objects.filter(Gelöscht=False, verordnetam=suche)|Spontanous.objects.filter(Gelöscht=False, DeltaP=suche)
    return render(request,'getspontanous.html', {"values": values})

@login_required(login_url='login')
@permission_required('osa_application.delete_spontanous',login_url='login')
def deletespontanous(request, id):
    value = Spontanous.objects.get(id=id)

    value.VerändertVon = request.user.id
    value.VerändertAm = datetime.datetime.now()
    value.Gelöscht = True
    value.save()

    values = Spontanous.objects.filter(Gelöscht=False)
    return render(request, 'getspontanous.html', {"values": values})

@login_required(login_url='login')
@permission_required('osa_application.change_spontanous',login_url='login')
def putspontanous_index(request, id):
    value = Spontanous.objects.get(id=id)
    return render(request, 'editspontanous.html', {"values": value})

@login_required(login_url='login')
@permission_required('osa_application.change_spontanous',login_url='login')
def putspontanous(request, id):
    value = Spontanous.objects.get(id=id)

    value.VerändertVon = request.user.id
    value.VerändertAm = datetime.datetime.now()
    value.Gelöscht = True
    value.save()

    Set = value.Set

    anzahl = Spontanous.objects.filter(Set=Set).order_by().values('Version').distinct().count()

    Version = anzahl + 1

    #eingabeID = request.POST.get("eingabeID")
    PatientID = request.POST.get("PatientID")
    IPAP = request.POST.get("IPAP")
    EPAP = request.POST.get("EPAP")
    DeltaP = request.POST.get("DeltaP")
    verordnetam = request.POST.get("verordnetam")



    VerändertVon = request.user.id
    VerändertAm = datetime.datetime.now()
    Gelöscht = False

    if PatientID == "":
        PatientID = None

    if IPAP == "":
        IPAP = None
    if EPAP == "":
        EPAP = None
    if DeltaP == "":
        DeltaP = None
    if verordnetam == "":
        verordnetam = None

    insert_txt = Spontanous(Set=Set,Version=Version, PatientID=PatientID, IPAP=IPAP, EPAP=EPAP,
                              DeltaP=DeltaP, verordnetam=verordnetam,VerändertVon=VerändertVon, VerändertAm=VerändertAm,
                              Gelöscht=Gelöscht)
    insert_txt.save()
    patients = Patient.objects.filter(Gelöscht=False)
    values = Spontanous.objects.filter(Gelöscht=False)
    return render(request, 'getspontanous.html', {"values": values,"patients":patients})











#Therapieabbruch
@login_required(login_url='login')
@permission_required('osa_application.add_therapieabbruch',login_url='login')
def posttherapieabbruch_index(request):
    all_patients = Patient.objects.filter(Gelöscht=False)
    return render(request, 'posttherapieabbruch.html', {"patients": all_patients})

@login_required(login_url='login')
@permission_required('osa_application.add_therapieabbruch',login_url='login')
def posttherapieabbruch(request):
    #EingabeID = request.POST.get("EingabeID")
    PatientID = request.POST.get("PatientID")
    Datum_Therapieabbruch = request.POST.get("Datum_Therapieabbruch")
    InfobezogenerTherapieabbruch = request.POST.get("InfobezogenerTherapieabbruch")

    if PatientID == "":
        PatientID = None
    if Datum_Therapieabbruch == "":
        Datum_Therapieabbruch = None
    if InfobezogenerTherapieabbruch == "":
        InfobezogenerTherapieabbruch = None

    anzahl = Firma.objects.order_by().values('Set').distinct().count()
    Set = anzahl + 1

    Version = 1

    VerändertVon = request.user.id
    VerändertAm = datetime.datetime.now()
    Gelöscht = False

    insert_txt = Therapieabbruch(Set=Set,Version=Version, PatientID=PatientID, InfobezogenerTherapieabbruch=InfobezogenerTherapieabbruch, Datum_Therapieabbruch=Datum_Therapieabbruch,VerändertVon=VerändertVon, VerändertAm=VerändertAm,Gelöscht=Gelöscht)
    insert_txt.save()
    values = Patient.objects.filter(Gelöscht=False)
    return render(request, 'posttherapieabbruch.html', {"patients": values})

@login_required(login_url='login')
@permission_required('osa_application.view_therapieabbruch',login_url='login')
def gettherapieabbruch(request):
    all_patients = Patient.objects.filter(Gelöscht=False)

    anzahl = Patient.objects.all().values('PatientID').annotate(total=Count('Version'))
    values = Therapieabbruch.objects.filter(Gelöscht=False)
    return render(request,'gettherapieabbruch.html', {"values": Paginator(values, 3).page(request.GET.get('page') or 1),"patients":Paginator(all_patients, 3).page(request.GET.get('page') or 1),"anzahl":Paginator(anzahl, 3).page(request.GET.get('page') or 1)})


def suchetherapieabbruch(request):
    suche = request.POST.get("suchen")
    if suche is None:
        suche = ""
    values = Therapieabbruch.objects.filter(Gelöscht=False, PatientID=suche)|Therapieabbruch.objects.filter(Gelöscht=False, Datum_Therapieabbruch=suche)|Therapieabbruch.objects.filter(Gelöscht=False, InfobezogenerTherapieabbruch=suche)
    return render(request,'gettherapieabbruch.html', {"values": values})

@login_required(login_url='login')
@permission_required('osa_application.delete_therapieabbruch',login_url='login')
def deletetherapieabbruch(request, id):
    value = Therapieabbruch.objects.get(id=id)

    value.VerändertVon = request.user.id
    value.VerändertAm = datetime.datetime.now()
    value.Gelöscht = True
    value.save()

    values = Therapieabbruch.objects.filter(Gelöscht=False)
    return render(request, 'gettherapieabbruch.html', {"values": values})

@login_required(login_url='login')
@permission_required('osa_application.update_therapieabbruch',login_url='login')
def puttherapieabbruch_index(request, id):
    value = Therapieabbruch.objects.get(id=id)
    return render(request, 'edittherapieabbruch.html', {"values": value})

@login_required(login_url='login')
@permission_required('osa_application.update_therapieabbruch',login_url='login')
def puttherapieabbruch(request, id):
    value = Therapieabbruch.objects.get(id=id)

    value.VerändertVon = request.user.id
    value.VerändertAm = datetime.datetime.now()
    value.Gelöscht = True
    value.save()

    #EingabeID = request.POST.get("EingabeID")
    PatientID = request.POST.get("PatientID")
    Datum_Therapieabbruch = request.POST.get("Datum_Therapieabbruch")
    InfobezogenerTherapieabbruch = request.POST.get("InfobezogenerTherapieabbruch")

    Set = value.Set

    anzahl = Therapieabbruch.objects.filter(Set=Set).order_by().values('Version').distinct().count()

    Version = anzahl + 1

    if PatientID == "":
        PatientID = None
    #if EingabeID == "":
     #   EingabeID = None
    if Datum_Therapieabbruch == "":
        Datum_Therapieabbruch = None
    if InfobezogenerTherapieabbruch == "":
        InfobezogenerTherapieabbruch = None

    VerändertVon = request.user
    VerändertAm = datetime.datetime.now()
    Gelöscht = False

    insert_txt = Therapieabbruch(Set=Set,Version=Version, PatientID=PatientID, InfobezogenerTherapieabbruch=InfobezogenerTherapieabbruch, Datum_Therapieabbruch=Datum_Therapieabbruch,VerändertVon=VerändertVon, VerändertAm=VerändertAm,Gelöscht=Gelöscht)
    insert_txt.save()

    values = Therapieabbruch.objects.filter(Gelöscht=False)
    return render(request, 'gettherapieabbruch.html', {"values": values})



