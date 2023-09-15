# Generated by Django 3.2.6 on 2022-01-22 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osa_application', '0026_remove_schlafbetreuender_arzt_arztid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medikament',
            fields=[
                ('Bezeichnung', models.CharField(default=None, max_length=255, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Medikament',
                'verbose_name_plural': 'Medikament',
                'db_table': 'osa_Medikament',
            },
        ),
        migrations.CreateModel(
            name='patient_medikamente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Patient', models.IntegerField(default=None)),
                ('Medikament', models.IntegerField(default=None)),
            ],
            options={
                'verbose_name': 'patient_medikamente',
                'verbose_name_plural': 'patient_medikamente',
                'db_table': 'osa_patient_medikamente',
            },
        ),
        migrations.RemoveField(
            model_name='autobitlevel',
            name='eingabeID',
        ),
        migrations.RemoveField(
            model_name='spontanous',
            name='eingabeID',
        ),
        migrations.RemoveField(
            model_name='spontanous_timed',
            name='eingabeID',
        ),
        migrations.RemoveField(
            model_name='therapieabbruch',
            name='EingabeID',
        ),
    ]