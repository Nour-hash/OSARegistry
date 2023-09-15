# Generated by Django 3.2.6 on 2021-12-14 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('osa_application', '0019_auto_20211214_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnosepsg',
            name='PatientID',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='osa_application.patient', unique=True),
        ),
        migrations.AlterField(
            model_name='asv',
            name='PatientID',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='asv',
            name='eingabeID',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='asv',
            name='maxEPAP',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='asv',
            name='maxPS',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='asv',
            name='minEPAP',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='asv',
            name='minPS',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='asv',
            name='verordnetam',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='cpap_einstellung',
            name='BeatmungsModi',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='cpap_einstellung',
            name='Datum_cpap',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='cpap_einstellung',
            name='EPAP',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='cpap_einstellung',
            name='Erweitert',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='cpap_einstellung',
            name='IPAP',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='cpap_einstellung',
            name='PatientID',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='cpap_kontrolle',
            name='Compliance_cpap',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='cpap_kontrolle',
            name='Datum_cpap',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='cpap_kontrolle',
            name='ModuswechselNotwendig',
            field=models.BooleanField(default=None),
        ),
        migrations.AlterField(
            model_name='cpap_kontrolle',
            name='PatientID',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='cpap_kontrolle',
            name='berücksichtigteTage_CPAP',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='cpap_kontrolle',
            name='durchschnittlicheVerwendungsdauer',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='cpap_kontrolle',
            name='nachjustierungNotwendig',
            field=models.BooleanField(default=None),
        ),
        migrations.AlterField(
            model_name='cpap_kontrolle',
            name='restAHibei_CPAP',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='diagnosepsg',
            name='AHI_Gesamt',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='diagnosepsg',
            name='BMI_bei_Diagnose_PSG',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='diagnosepsg',
            name='Datum_Diagnose_PSG',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='diagnosepsg',
            name='Diagnose',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='diagnosepsg',
            name='Dominanz',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='diagnosepsg',
            name='Lageabhängig',
            field=models.BooleanField(default=None),
        ),
        migrations.AlterField(
            model_name='diagnosepsg',
            name='O2unter90Prozent',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='diagnosepsg',
            name='REM_assoziert',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='diagnosepsg',
            name='SaO2min_PSG',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='diagnosepsg',
            name='Zustimmung_für_Beatmung',
            field=models.BooleanField(default=None),
        ),
        migrations.AlterField(
            model_name='diagnosepsg',
            name='alternative_Therapieempfehlung',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='diagnosepsg',
            name='primäre_Therapieempfehlung',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='firma',
            name='Firmenname',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='gerät',
            name='Freitext',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='gerät',
            name='Gerätename',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='gerät',
            name='Heizschlauch',
            field=models.BooleanField(default=None),
        ),
        migrations.AlterField(
            model_name='gerät',
            name='Hersteller',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='gerät',
            name='Modi',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='gerät',
            name='O2Anschluss',
            field=models.BooleanField(default=None),
        ),
        migrations.AlterField(
            model_name='gerät',
            name='Rampe',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='gerät',
            name='WLB',
            field=models.BooleanField(default=None),
        ),
        migrations.AlterField(
            model_name='gerät',
            name='vertreibendeFirma',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='masken',
            name='Größe',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='masken',
            name='Hersteller',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='masken',
            name='Maskenname',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='masken',
            name='Maskentyp',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='masken',
            name='PatientID',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='schlafbetreudender_arzt',
            name='ArztID',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='schlafbetreudender_arzt',
            name='Email',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='schlafbetreudender_arzt',
            name='Fachrichtung',
            field=models.CharField(default=None, max_length=55),
        ),
        migrations.AlterField(
            model_name='schlafbetreudender_arzt',
            name='Hausnummer',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='schlafbetreudender_arzt',
            name='Name',
            field=models.CharField(default=None, max_length=55),
        ),
        migrations.AlterField(
            model_name='schlafbetreudender_arzt',
            name='Ort',
            field=models.CharField(default=None, max_length=55),
        ),
        migrations.AlterField(
            model_name='schlafbetreudender_arzt',
            name='Strasse',
            field=models.CharField(default=None, max_length=55),
        ),
        migrations.AlterField(
            model_name='schlafbetreudender_arzt',
            name='Telefonnummer',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='schlafbetreudender_arzt',
            name='Vorhanden',
            field=models.BooleanField(default=None),
        ),
        migrations.AlterField(
            model_name='schlafbetreudender_arzt',
            name='plz',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='vorscreening',
            name='DatumderPG',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='vorscreening',
            name='EingabeID',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='vorscreening',
            name='PGdurchgeführtvon',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='vorscreening',
            name='RDI',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='vorscreening',
            name='sao2minPG',
            field=models.IntegerField(default=None),
        ),
    ]