# Generated by Django 3.2.6 on 2022-01-13 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('osa_application', '0024_alter_patient_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asv',
            name='eingabeID',
        ),
        migrations.RemoveField(
            model_name='avaps',
            name='EingabeID',
        ),
    ]