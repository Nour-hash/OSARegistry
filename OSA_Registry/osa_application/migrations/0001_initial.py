# Generated by Django 3.2.6 on 2021-10-26 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='g_Gerät',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gerätename', models.CharField(max_length=255)),
                ('Hersteller', models.CharField(max_length=255)),
                ('vertreibendeFirma', models.CharField(max_length=255)),
                ('Modi', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='p_Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SVNummer', models.IntegerField()),
                ('Geburtsdatum', models.DateField()),
                ('Vorname', models.CharField(max_length=55)),
                ('Nachname', models.CharField(max_length=55)),
                ('Geschlecht', models.CharField(max_length=10)),
                ('Vorscreening', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='sa_SchlafbetreuenderArzt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SchlafbetreuenderArzt', models.CharField(max_length=255)),
                ('Fachrichtung', models.CharField(max_length=255)),
                ('PLZ', models.IntegerField()),
                ('Ort', models.CharField(max_length=255)),
                ('Straße', models.CharField(max_length=255)),
                ('Hausnummer', models.IntegerField()),
                ('TelefonNummer', models.IntegerField()),
                ('PatientID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='osa_application.p_patient')),
            ],
        ),
        migrations.CreateModel(
            name='f_Firma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firma', models.CharField(max_length=255)),
                ('PatientID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='osa_application.p_patient')),
            ],
        ),
        migrations.CreateModel(
            name='com_Compliance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Datum', models.DateField()),
                ('Compliance', models.CharField(max_length=255)),
                ('BerücksichtigteTage', models.IntegerField()),
                ('DurchschnitVerwendung', models.CharField(max_length=255)),
                ('restAHI', models.CharField(max_length=255)),
                ('PatientID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='osa_application.p_patient')),
            ],
        ),
    ]
