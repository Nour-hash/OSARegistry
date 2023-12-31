# Generated by Django 3.2.6 on 2022-01-27 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osa_application', '0032_remove_vorscreening_eingabeid'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ASV',
        ),
        migrations.DeleteModel(
            name='autoBitLevel',
        ),
        migrations.DeleteModel(
            name='AVAPS',
        ),
        migrations.DeleteModel(
            name='Spontanous_Timed',
        ),
        migrations.RenameField(
            model_name='cpap_einstellung',
            old_name='EPAP',
            new_name='Zielvolumen',
        ),
        migrations.AddField(
            model_name='cpap_einstellung',
            name='maxEPAP',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='cpap_einstellung',
            name='maxPS',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='cpap_einstellung',
            name='minEPAP',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='cpap_einstellung',
            name='minPS',
            field=models.IntegerField(default=None),
        ),
    ]
