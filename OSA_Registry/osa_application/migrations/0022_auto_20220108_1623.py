# Generated by Django 3.2.6 on 2022-01-08 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osa_application', '0021_auto_20220107_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='Geburtsdatum',
            field=models.DateField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='SVNummer',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
