# Generated by Django 3.2.6 on 2021-11-19 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('osa_application', '0010_rename_straße_sa_schlafbetreuenderarzt_strasse'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='p_patient',
            table='p_Patient',
        ),
    ]
