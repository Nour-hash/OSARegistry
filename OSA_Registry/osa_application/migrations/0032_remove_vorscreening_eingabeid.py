# Generated by Django 3.2.6 on 2022-01-22 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('osa_application', '0031_auto_20220122_1716'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vorscreening',
            name='EingabeID',
        ),
    ]