# Generated by Django 3.2.6 on 2022-01-29 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osa_application', '0036_auto_20220128_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vorscreening',
            name='PGdurchgeführtvon',
            field=models.IntegerField(blank=True, default=None),
        ),
    ]
