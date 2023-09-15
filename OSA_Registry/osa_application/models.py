import datetime
from django import forms
from django.db import models
from django.utils import timezone



class Patient(models.Model):
    SVNummer = models.IntegerField(default=None,blank=True)
    Geburtsdatum = models.DateField(default=None,null=True,blank=True)
    Vorname = models.CharField(max_length=55,default=None,blank=True)
    Nachname = models.CharField(max_length=55,default=None,blank=True)
    Geschlecht = models.CharField(max_length=10,default=None,blank=True)
    Vorscreening = models.BooleanField(max_length=10,default=None,blank=True)

    PatientID = models.IntegerField(default=None,blank=True)
    Version = models.IntegerField(default=None,blank=True)
    VerändertVon = models.CharField(max_length=55,default=None)
    VerändertAm = models.DateTimeField(default=None)
    Gelöscht = models.BooleanField(max_length=10,default=None)
    #Arzt = models.ForeignKey(sba_Schlafbetreudender_Arzt,on_delete=models.CASCADE,default=None)
    class Meta:
        db_table="osa_Patient"

        verbose_name = ' Patient'
        verbose_name_plural = ' Patient'


class Firma(models.Model):
    Firmenname = models.CharField(max_length=255,default=None,blank=True)

    Set = models.IntegerField(default=None,blank=True)
    Version = models.IntegerField(default=None,blank=True)
    VerändertVon = models.CharField(max_length=55,default=None)
    VerändertAm = models.DateTimeField(default=None)
    Gelöscht = models.BooleanField(max_length=10,default=None)
    class Meta:
        db_table="osa_Firmen"

        verbose_name = 'Firma'
        verbose_name_plural = 'Firma'

class Vorscreening(models.Model):
    PGdurchgeführtvon = models.IntegerField(default=None,blank=True)
    DatumderPG = models.DateField(default=None,blank=True)
    sao2minPG = models.IntegerField(default=None,blank=True)
    RDI = models.IntegerField(default=None,blank=True)
    #EingabeID = models.IntegerField(default=None)

    Set = models.IntegerField(default=None,blank=True)
    Version = models.IntegerField(default=None,blank=True)
    VerändertVon = models.CharField(max_length=55,default=None)
    VerändertAm = models.DateTimeField(default=None)
    Gelöscht = models.BooleanField(max_length=10,default=None)
    class Meta:
        db_table = "osa_Vorscreening"

        verbose_name = 'Vorscreening'
        verbose_name_plural = 'Vorscreening'

class Masken(models.Model):
    PatientID = models.IntegerField(default=None,blank=True)
    Maskentyp = models.CharField(max_length=255,default=None,blank=True)
    Maskenname = models.CharField(max_length=255,default=None,blank=True)
    Hersteller = models.CharField(max_length=255,default=None,blank=True)
    Größe = models.CharField(max_length=255,default=None,blank=True)

    Set = models.IntegerField(default=None,blank=True)
    Version = models.IntegerField(default=None,blank=True)
    VerändertVon = models.CharField(max_length=55,default=None)
    VerändertAm = models.DateTimeField(default=None)
    Gelöscht = models.BooleanField(max_length=10,default=None)
    class Meta:
        db_table = "osa_Masken"

        verbose_name = 'Masken'
        verbose_name_plural = 'Masken'

class Gerät(models.Model):
    PatientID = models.IntegerField(default=None,blank=True)
    Gerätename = models.CharField(max_length=255,default=None,blank=True)
    Hersteller = models.CharField(max_length=255,default=None,blank=True)
    vertreibendeFirma = models.IntegerField(default=None,blank=True)
    Modi = models.CharField(max_length=255,default=None,blank=True)
    WLB = models.BooleanField(default=None,blank=True)
    Rampe = models.IntegerField(default=None,blank=True)
    O2Anschluss = models.BooleanField(default=None,blank=True)
    Heizschlauch = models.BooleanField(default=None,blank=True)
    Freitext = models.CharField(max_length=255,default=None,blank=True)

    Set = models.IntegerField(default=None,blank=True)
    Version = models.IntegerField(default=None,blank=True)
    VerändertVon = models.CharField(max_length=55,default=None)
    VerändertAm = models.DateTimeField(default=None)
    Gelöscht = models.BooleanField(max_length=10,default=None)

    class Meta:
        db_table = "osa_Gerät"

        verbose_name = 'Gerät'
        verbose_name_plural = 'Gerät'

    def __str__(self):
        return self.Gerät_text


class Schlafbetreuender_Arzt(models.Model):
    Vorhanden = models.BooleanField(default=None,blank=True)
    Name= models.CharField(max_length=55,default=None,blank=True)
    Fachrichtung= models.CharField(max_length=55,default=None,blank=True)
    plz = models.IntegerField(default=None,blank=True)
    Ort= models.CharField(max_length=55,default=None,blank=True)
    Strasse= models.CharField(max_length=55,default=None,blank=True)
    Hausnummer = models.IntegerField(default=None,blank=True)
    Telefonnummer = models.IntegerField(default=None,blank=True)
    Email = models.CharField(max_length=255,default=None,blank=True)
    #ArztID = models.IntegerField(default=None)

    Set = models.IntegerField(default=None,blank=True)
    Version = models.IntegerField(default=None,blank=True)
    VerändertVon = models.CharField(max_length=55,default=None)
    VerändertAm = models.DateTimeField(default=None)
    Gelöscht = models.BooleanField(max_length=10,default=None)
    class Meta:
        db_table = "osa_Schlafbetreuender_Arzt"
        verbose_name = 'Schlafbetreuender_Arzt'
        verbose_name_plural = 'Schlafbetreuender_Arzt'

    def __str__(self):
        return self.Schlafbetreuender_Arzt_text

class DiagnosePSG(models.Model):
    Datum_Diagnose_PSG = models.DateField(default=None,blank=True)
    PatientID = models.IntegerField(default=None,blank=True)
    BMI_bei_Diagnose_PSG = models.IntegerField(default=None,blank=True)
    SaO2min_PSG = models.IntegerField(default=None,blank=True)
    Dominanz = models.CharField(max_length=255,default=None,blank=True)
    Lageabhängig = models.BooleanField(default=None,blank=True)
    AHI_Gesamt = models.IntegerField(default=None,blank=True)
    REM_assoziert = models.IntegerField(default=None,blank=True)
    O2unter90Prozent = models.IntegerField(default=None,blank=True)
    Diagnose = models.CharField(max_length=255,default=None,blank=True)
    primäre_Therapieempfehlung = models.CharField(max_length=255,default=None,blank=True)
    alternative_Therapieempfehlung = models.CharField(max_length=255,default=None,blank=True)
    Zustimmung_für_Beatmung = models.BooleanField(default=None,blank=True)

    Set = models.IntegerField(default=None,blank=True)
    Version = models.IntegerField(default=None,blank=True)
    VerändertVon = models.CharField(max_length=55,default=None)
    VerändertAm = models.DateTimeField(default=None)
    Gelöscht = models.BooleanField(max_length=10,default=None)

    class Meta:
        db_table = "osa_DiagnosePSG"

        verbose_name = 'DiagnosePSG'
        verbose_name_plural = 'DiagnosePSG'

    def __str__(self):
        return self.DiagnosePSG_text

class CPAP_Einstellung(models.Model):
    PatientID = models.IntegerField(default=None,blank=True)
    Datum_cpap = models.DateField(default=None,blank=True)
    minEPAP = models.IntegerField(default=None,blank=True)
    maxEPAP = models.IntegerField(default=None,blank=True)
    minPS = models.IntegerField(default=None,blank=True)
    maxPS = models.IntegerField(default=None,blank=True)
    Zielvolumen = models.IntegerField(default=None,blank=True)
    BeatmungsModi = models.CharField(max_length=255,default=None,blank=True)
    IPAP = models.IntegerField(default=None,blank=True)
    Erweitert = models.CharField(max_length=255,default=None,blank=True)

    Set = models.IntegerField(default=None,blank=True)
    Version = models.IntegerField(default=None,blank=True)
    VerändertVon = models.CharField(max_length=55,default=None)
    VerändertAm = models.DateTimeField(default=None)
    Gelöscht = models.BooleanField(max_length=10,default=None)

    class Meta:
        db_table = "osa_CPAP_Einstellung"

        verbose_name = 'CPAP_Einstellung'
        verbose_name_plural = 'CPAP_Einstellung'


class CPAP_Kontrolle(models.Model):
    PatientID = models.IntegerField(default=None,blank=True)
    Datum_cpap = models.DateField(default=None,blank=True)
    Compliance_cpap = models.IntegerField(default=None,blank=True)
    durchschnittlicheVerwendungsdauer = models.IntegerField(default=None,blank=True)
    berücksichtigteTage_CPAP = models.IntegerField(default=None,blank=True)
    restAHibei_CPAP = models.IntegerField(default=None,blank=True)
    nachjustierungNotwendig = models.BooleanField(default=None,blank=True)
    ModuswechselNotwendig = models.BooleanField(default=None,blank=True)

    Set = models.IntegerField(default=None,blank=True)
    Version = models.IntegerField(default=None,blank=True)
    VerändertVon = models.CharField(max_length=55,default=None)
    VerändertAm = models.DateTimeField(default=None)
    Gelöscht = models.BooleanField(max_length=10,default=None)

    class Meta:
        db_table = "osa_CPAP_Kontrolle"

        verbose_name = 'CPAP_Kontrolle'
        verbose_name_plural = 'CPAP_Kontrolle'



class Spontanous(models.Model):
    #eingabeID = models.IntegerField(default=None)
    PatientID = models.IntegerField(default=None,blank=True)
    verordnetam = models.DateField(default=None,blank=True)
    IPAP = models.IntegerField(default=None,blank=True)
    EPAP = models.IntegerField(default=None,blank=True)
    DeltaP = models.IntegerField(default=None,blank=True)

    Set = models.IntegerField(default=None,blank=True)
    Version = models.IntegerField(default=None,blank=True)
    VerändertVon = models.CharField(max_length=55,default=None)
    VerändertAm = models.DateTimeField(default=None)
    Gelöscht = models.BooleanField(max_length=10,default=None)

    class Meta:
        db_table = "osa_Spontanous"

        verbose_name = 'Spontanous'
        verbose_name_plural = 'Spontanous'


class Therapieabbruch(models.Model):
    #EingabeID  = models.IntegerField(default=None)
    PatientID = models.IntegerField(default=None,blank=True)
    Datum_Therapieabbruch  = models.DateField(default=None,blank=True)
    InfobezogenerTherapieabbruch  = models.CharField(max_length=255,default=None,blank=True)

    Set = models.IntegerField(default=None,blank=True)
    Version = models.IntegerField(default=None,blank=True)
    VerändertVon = models.CharField(max_length=55,default=None)
    VerändertAm = models.DateTimeField(default=None)
    Gelöscht = models.BooleanField(max_length=10,default=None)

    class Meta:
        db_table = "osa_Therapieabbruch"
        verbose_name = 'Therapieabbruch'
        verbose_name_plural = 'Therapieabbruch'

class Medikament (models.Model):
    Bezeichnung = models.CharField(max_length=255,default=None,primary_key=True)

    class Meta:
        db_table = "osa_Medikament"
        verbose_name = 'Medikament'
        verbose_name_plural = 'Medikament'

class patient_medikamente(models.Model):
    Patient = models.IntegerField(default=None,blank=True)
    Medikament = models.CharField(max_length=255,default=None,blank=True)

    Set = models.IntegerField(default=None,blank=True)
    Version = models.IntegerField(default=None,blank=True)
    VerändertVon = models.CharField(max_length=55,default=None)
    VerändertAm = models.DateTimeField(default=None)
    Gelöscht = models.BooleanField(max_length=10,default=None)

    class Meta:
        db_table = "osa_patient_medikamente"
        verbose_name = 'patient_medikamente'
        verbose_name_plural = 'patient_medikamente'


