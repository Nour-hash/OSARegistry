# Generated by Django 3.2.6 on 2021-11-19 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('osa_application', '0008_remove_sa_schlafbetreuenderarzt_patientid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='p_patient',
            name='Arzt',
        ),
    ]
