# Generated by Django 3.2.6 on 2021-12-13 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osa_application', '0016_alter_spontanous_timed_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='asv',
            name='Gelöscht',
            field=models.BooleanField(default=None, max_length=10),
        ),
        migrations.AddField(
            model_name='asv',
            name='VerändertAm',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='asv',
            name='VerändertVon',
            field=models.CharField(default=None, max_length=55),
        ),
        migrations.AddField(
            model_name='autobitlevel',
            name='Gelöscht',
            field=models.BooleanField(default=None, max_length=10),
        ),
        migrations.AddField(
            model_name='autobitlevel',
            name='VerändertAm',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='autobitlevel',
            name='VerändertVon',
            field=models.CharField(default=None, max_length=55),
        ),
        migrations.AddField(
            model_name='avaps',
            name='Gelöscht',
            field=models.BooleanField(default=None, max_length=10),
        ),
        migrations.AddField(
            model_name='avaps',
            name='VerändertAm',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='avaps',
            name='VerändertVon',
            field=models.CharField(default=None, max_length=55),
        ),
        migrations.AddField(
            model_name='cpap_einstellung',
            name='Gelöscht',
            field=models.BooleanField(default=None, max_length=10),
        ),
        migrations.AddField(
            model_name='cpap_einstellung',
            name='VerändertAm',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='cpap_einstellung',
            name='VerändertVon',
            field=models.CharField(default=None, max_length=55),
        ),
        migrations.AddField(
            model_name='cpap_kontrolle',
            name='Gelöscht',
            field=models.BooleanField(default=None, max_length=10),
        ),
        migrations.AddField(
            model_name='cpap_kontrolle',
            name='VerändertAm',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='cpap_kontrolle',
            name='VerändertVon',
            field=models.CharField(default=None, max_length=55),
        ),
        migrations.AddField(
            model_name='diagnosepsg',
            name='Gelöscht',
            field=models.BooleanField(default=None, max_length=10),
        ),
        migrations.AddField(
            model_name='diagnosepsg',
            name='VerändertAm',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='diagnosepsg',
            name='VerändertVon',
            field=models.CharField(default=None, max_length=55),
        ),
        migrations.AddField(
            model_name='firma',
            name='Gelöscht',
            field=models.BooleanField(default=None, max_length=10),
        ),
        migrations.AddField(
            model_name='firma',
            name='VerändertAm',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='firma',
            name='VerändertVon',
            field=models.CharField(default=None, max_length=55),
        ),
        migrations.AddField(
            model_name='gerät',
            name='Gelöscht',
            field=models.BooleanField(default=None, max_length=10),
        ),
        migrations.AddField(
            model_name='gerät',
            name='VerändertAm',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='gerät',
            name='VerändertVon',
            field=models.CharField(default=None, max_length=55),
        ),
        migrations.AddField(
            model_name='masken',
            name='Gelöscht',
            field=models.BooleanField(default=None, max_length=10),
        ),
        migrations.AddField(
            model_name='masken',
            name='VerändertAm',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='masken',
            name='VerändertVon',
            field=models.CharField(default=None, max_length=55),
        ),
        migrations.AddField(
            model_name='schlafbetreudender_arzt',
            name='Gelöscht',
            field=models.BooleanField(default=None, max_length=10),
        ),
        migrations.AddField(
            model_name='schlafbetreudender_arzt',
            name='VerändertAm',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='schlafbetreudender_arzt',
            name='VerändertVon',
            field=models.CharField(default=None, max_length=55),
        ),
        migrations.AddField(
            model_name='spontanous',
            name='Gelöscht',
            field=models.BooleanField(default=None, max_length=10),
        ),
        migrations.AddField(
            model_name='spontanous',
            name='VerändertAm',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='spontanous',
            name='VerändertVon',
            field=models.CharField(default=None, max_length=55),
        ),
        migrations.AddField(
            model_name='spontanous_timed',
            name='Gelöscht',
            field=models.BooleanField(default=None, max_length=10),
        ),
        migrations.AddField(
            model_name='spontanous_timed',
            name='VerändertAm',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='spontanous_timed',
            name='VerändertVon',
            field=models.CharField(default=None, max_length=55),
        ),
        migrations.AddField(
            model_name='therapieabbruch',
            name='Gelöscht',
            field=models.BooleanField(default=None, max_length=10),
        ),
        migrations.AddField(
            model_name='therapieabbruch',
            name='VerändertAm',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='therapieabbruch',
            name='VerändertVon',
            field=models.CharField(default=None, max_length=55),
        ),
        migrations.AddField(
            model_name='vorscreening',
            name='Gelöscht',
            field=models.BooleanField(default=None, max_length=10),
        ),
        migrations.AddField(
            model_name='vorscreening',
            name='VerändertAm',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='vorscreening',
            name='VerändertVon',
            field=models.CharField(default=None, max_length=55),
        ),
    ]
